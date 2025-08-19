from __future__ import annotations
from typing import Any

from .cfgParms import *
from .liveIP import *
import requests
import json, csv, re
import logging
import datetime
import tqdm
from tenacity import retry

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

DEFAULT_TIMEDELTA = datetime.timedelta(minutes=5)


class xtviaServer:
    def __init__(
        self,
        serverIP: str,
        configsToCollect: list,
        inspection: int = 10,
        sessionID: str = "Reset",
        singleParam: str = None,
    ) -> None:
        self._serverIP: str = serverIP
        self._facilityName: str = None
        self._chassis: str = None
        self._version: str = None
        self._SN: str = None
        self._sessionID: str = sessionID
        self._HWEdition: str = None
        self._serverStatus: int = None
        self._latestMCInfo: dict = None
        self._technicalLocked: bool = None
        self._lastUpdateTS: datetime.datetime = None
        self._foucsConfigLines: list = configsToCollect
        self._configs: dict[int, configLine] = {}
        self._liveIPs: dict[int, LiveIPConfig] = {}
        self._options: dict[int, bool] = {}

        if inspection >= 1:
            self._get_multicam_info()
        if inspection >= 2:
            self._get_server_status()
        if inspection >= 3:
            self._get_options()
        if inspection >= 4:
            self._get_configs(singleParam)
        if inspection >= 5:
            self._get_liveips()

        if singleParam is not None:
            self._get_configs(singleParam)

    def __str__(self) -> str:
        return (
            f"ServerIP: {self._serverIP}, Facility Name: {self._facilityName}, Version: {self._version}, SN: {self._SN}"
        )

    # Operationally Some Very Generic Functions

    def _isInfoStale(self) -> bool:
        """Checks if the connection to the server is stale and should be updated.

        Returns:
            bool: Retruns True if stale
        """
        if self._lastUpdateTS is None:
            logger.debug("No last update time set. Returning True.")
            return True
        if self._lastUpdateTS + DEFAULT_TIMEDELTA < datetime.datetime.now():
            logger.debug("Time is stale, returning True.")
            return True
        else:
            return False

    def _get_SessionID(self, checkStale: bool = False) -> str:
        """Gets the current session ID, this also handles checking if the info is stale and resets if need be.

        Args:
            checkStale (bool, optional): If you want to override the stale check, you can set this to False. Defaults to True.

        Returns:
            str: The current session ID.
        """

        #  If the info is stale, then we need to get the info again.
        if self._isInfoStale() and checkStale:
            self._get_multicam_info()

        # If the SessionID is Reset then we need to start by getting Multicam Info, then we can continue.
        if self._sessionID == "Reset":
            self._get_multicam_info()

        # Finally return the Session ID
        return self._sessionID

    def _get_request(self, url: str, parms: dict) -> dict:
        """Handles all basic HTTP GET Requests to the server.

        Args:
            url (str): URL for the request.
            parms (dict): Parameters for the request. Should include the SessionID and any others for needed.

        Raises:
            e: IF there is an issue with the request, it will raise an error.

        Returns:
            dict: Returns the JSON data from the request.
        """
        response = requests.get(url, params=parms)

        # Since VIAs can only have one Session Open with the server, if another person takes the session while using the server, it will leave us with a 403 Unauthorized error.
        if response.status_code == 403:
            logger.debug("SessionID is invalid, resetting it")
            parms["SessionID"] = "Reset"
            response = requests.get(url, params=parms)
        try:
            data = response.json()
            return data
        except Exception as e:
            logger.error(f"Error getting request: {e} could not get json data")
            raise e

    def _post_request(self, url: str, params: dict, data: dict) -> dict:
        """Handles all post requests for the server, it will handle bad sessions data.

        Args:
            url (str): URL for Request.
            params (dict): Any Query Parameters you may want to send along
            data (dict): Dictionary of data to send.

        Returns:
            dict: Returns the JSON data from the request.
        """
        response = requests.post(url, params=params, data=data)

        # This will handle any bad sessions and try to reset it.
        if response.status_code == 403:
            logger.debug("SessionID is invalid, resetting it")
            params["SessionID"] = "Reset"
            response = requests.post(url, params=params, data=data)

        data = response.json()

    # Server Private Functions
    # Most of these are used ini initalizing the class

    def _get_multicam_info(self) -> dict:
        """Gets the Multicam Info from the Server.

        Args:
            serverIP (str): IP address of the server you want to get info about.

        Returns:
            dict: A large dictionary containing all the info you could ever want.
        """

        # This is the only instance where it is appropriate to ignore the getSessionID() function, but since it could cause a loop I figure this is better.
        parms = {"SessionID": self._sessionID}
        url = f"http://{self._serverIP}/cfgweb/CfgWeb.dll/MulticamInfoJS"

        try:
            data = self._get_request(url, parms)
            self._facilityName = data["FacilityName"]
            self._chassis = data["Chassis"]
            self._version = data["Version"]
            self._SN = data["SN"]
            self._technicalLocked = data["IsTechnicalLocked"]
            self._HWEdition = data["HWEdition"]
            self._sessionID = data["SessionID"]
            self._latestMCInfo = data
            self._lastUpdateTS = datetime.datetime.now()
            return data
        except Exception as e:
            raise e

    def _get_options(self):
        parms = {"SessionID": self._get_SessionID()}
        url = f"http://{self._serverIP}/cfgweb/CfgWeb.dll/OptionCodesJS"

        rawdata = self._get_request(url, parms)
        data = rawdata["Options"]

        for i in data:
            self._options[i["Code"]] = i["Name"]

        return data

    def _get_configs(self, singleParam: str = None):
        for i in self._foucsConfigLines:
            self._configs[i] = configLine(
                numLine=i,
                readFunc=self._get_configLine_all,
                updateFunc=self._update_configLine,
                readParam=self._get_configLine_param,
                singleParam=singleParam,
            )

    def _get_liveips(self):
        for i in tqdm.tqdm(self._foucsConfigLines, desc="Getting Live IP Configs"):
            i = i + 1
            self._set_liveIP_cfglineNum(i)
            data = self._get_liveip_all()
            self._liveIPs[i] = LiveIPConfig(
                data=data,
                updateFunc=self._set_liveip_one,
                readFunc=self._get_liveip_one,
                numLine=i,
            )

    def _get_server_status(self) -> int:
        """Gets the state of the server, if MC is running or not.

        Args:
            serverIP (str): IP address of the server you want to get info about.

        Returns:
            int: -1 = Not use what state it is in.
                 0 = Not Running Not Reachable # Not Yet Implemented
                 1 = Multicam Setup is running
                 2 = Multicam is running
        """
        if self._isInfoStale():
            self._get_multicam_info()

        if self._latestMCInfo["IsMulsetupRunning"] == True:
            self._serverStatus = 1
        elif self._latestMCInfo["IsMulticamRunning"] == True:
            self._serverStatus = 2
        else:
            self._serverStatus = -1

        return self._serverStatus

    # Private Config Line Functions

    def _get_configLine_all(self, numLine: int) -> dict:
        parms = {"SessionID": self._get_SessionID(), "NumLine": numLine, "Meta": True, "All": True}
        url = f"http://{self._serverIP}/cfgweb/CfgWeb.dll/GetConfigValuesJS"

        data = self._get_request(url, parms)

        return data

    def _get_configLine_param(self, param: str, numLine: int) -> str:

        parms = {"SessionID": self._get_SessionID(False), "NumLine": numLine, "ParamName": param, "List": True}
        url = f"http://{self._serverIP}/cfgweb/CfgWeb.dll/ParamDescriptorJS"

        logger.debug(f"Getting description for {param} at line {numLine}")

        data = self._get_request(url, parms)

        return data

    def _update_configLine(self, numLine: int, cfgName: str, cfgValue: Any, save: bool = False) -> dict:

        params: dict = {
            cfgName: cfgValue,
            "NumLine": numLine,
            "SessionID": self._get_SessionID(),
            "Commit": save,
            "Save": save,
        }
        url = f"http://{self._serverIP}/cfgweb/CfgWeb.dll/SetConfigValuesJS"

        data = self._get_request(url, params)

        return data

    # Private LiveIP Functions

    def _get_liveip_all(self) -> dict:
        params = {
            "SessionID": self._get_SessionID(False),
        }
        url = f"http://{self._serverIP}/ipconfigurationweb/getsubtreeactionjs"

        data = self._get_request(url, params)

        return data

    def _get_liveip_one(self, numLine: int, uri: str) -> dict:

        self._set_liveIP_cfglineNum(numLine)

        params = {"SessionID": self._get_SessionID(False)}
        data = {"uris": uri}
        url = f"http://{self._serverIP}/ipconfigurationweb/getparameterlistactionjs"

        response = self._post_request(url, params, data)

        return response

    def _set_liveIP_cfglineNum(self, num: int) -> dict:

        params = {
            "SessionID": self._get_SessionID(False),
            "number": num,
        }
        url = f"http://{self._serverIP}/ipconfigurationweb/setlinenumberactionjs"

        data = self._get_request(url, params)

        logger.debug(f"Updated Live IP Config Line Number to {num}")
        return data

    def _set_liveip_one(self, numLine: int, uri: str, value: Any) -> dict:
        self._set_liveIP_cfglineNum(numLine)
        params = {"SessionID": self._get_SessionID(False)}
        data = {"uri": uri, "value": value}
        url = f"http://{self._serverIP}/ipconfigurationweb/setparametervalueactionjs"
        response = self._post_request(url, params, data)

        self._commit_liveIP()

        return response

    def _commit_liveIP(self) -> dict:
        params = {"SessionID": self._get_SessionID(False)}
        url = f"http://{self._serverIP}/ipconfigurationweb/commitactionjs"
        data = self._get_request(url, params)
        return data

    # Public Functions to get Information about the server

    def get_facility_name(self) -> str:
        if self._isInfoStale():
            self._get_multicam_info()
        return self._facilityName

    def set_facility_name(self, name: str):
        if self._isInfoStale():
            self._get_multicam_info()

        # Sets the Facility Name of the server
        self._post_request(
            url=f"http://{self._serverIP}/cfgweb/CfgWeb.dll/FacilityNameJS",
            params={"FacilityName": name, "SessionID": self._get_SessionID()},
            data={},
        )

        # Then Lets Update MC info and Checkit out
        self._get_multicam_info()

        # if self.get_facility_name() != name:
        #    raise Exception("Failed to set Facility Name")

        self._facilityName = name

    def get_state(self) -> int:
        if self._isInfoStale():
            self._get_multicam_info()
        return self._serverStatus

    def get_chassis(self) -> str:
        if self._isInfoStale():
            self._get_multicam_info()
        return self._chassis

    def get_version(self) -> str:
        if self._isInfoStale():
            self._get_multicam_info()
        return self._version

    def get_SN(self) -> str:
        if self._isInfoStale():
            self._get_multicam_info()
        return self._SN

    def get_technical_lock(self) -> bool:
        if self._isInfoStale():
            self._get_multicam_info()
        return self._technicalLocked

    def get_mc_info_parm(self, parmName: str) -> Any:

        if self._isInfoStale():
            self._get_multicam_info()
        return self._latestMCInfo[parmName]

    def get_options(self) -> dict:
        if self._isInfoStale():
            self._get_multicam_info()
        return self._options

    def get_configs(self) -> dict[int, configLine]:
        if self._isInfoStale():
            self._get_multicam_info()
        return self._configs

    def get_config(self, i: int) -> configLine:
        if self._isInfoStale():
            self._get_multicam_info()
        return self._configs[i]

    def get_liveips(self) -> dict[int, LiveIPConfig]:
        return self._liveIPs

    def get_liveip(self, i: int) -> LiveIPConfig:
        return self._liveIPs[i]

    def get_serverIP(self) -> str:
        return self._serverIP

    def get_HWEdition(self) -> str:
        return self._HWEdition

    # This gets all the data about the server as a dictionary, including the configlines, it can be very large.

    def dict(self) -> dict:
        result = {
            "ServerIP": self._serverIP,
            "FacilityName": self._facilityName,
            "Version": self._version,
            "SN": self._SN,
            "Options": self._options,
            "Configs": {},
            "LiveIPs": {},
        }
        # Configs would look something like
        # { Configs : {1 : [NAME:{}]}

        # Config Info.
        for i in tqdm.tqdm(self._configs.keys(), desc=f"Building Dict for Config Lines"):
            tempCfgParms = self._configs[i]
            result["Configs"][i] = tempCfgParms.data()

        # For Live IP Info
        for i in tqdm.tqdm(self._liveIPs.keys(), desc=f"Building Dict for Live IP Configs"):
            result["LiveIPs"][i] = self._liveIPs[i].data()
        return result


if __name__ == "__main__":
    server = xtviaServer("10.10.52.101", [1], singleParam="CFG_PARAM_VIDEO_3G_DUAL_MODE", inspection=2)
    print(server)
    # json.dump(server.dict(), open("deubg_pre.json", "w"))
    print(server.dict())
    print("Updateing a value in configLine 1")
    server.get_config(1).get_param("CFG_PARAM_VIDEO_3G_DUAL_MODE").setCurrentValue("3G Level-A")
    # server.get_liveip(1).getInput(1).get_video(1).get_stream().set_destinationAddress("239.239.201.1")

    # json.dump(server.dict(), open("debug_post.json", "w"))
