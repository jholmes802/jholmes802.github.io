# liveIPBuild.yaml

This is a custom python script that convers the LiveIP CSV sheets we have into more machine readable JSON files. 

```python
#!/usr/bin/python3

from __future__ import absolute_import, division, print_function

__metaclass__ = type
import csv, json
import argparse
import requests
import re
import tqdm
import os
import logging
from ansible.module_utils.basic import AnsibleModule


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEBUG = False


def loadIPJson(serverIP: str, liveIPSourceFile: str) -> tuple[str, dict]:
    """Provided the Server Number and the location of the work sheet file, this can create a JSON
     file containing the needed JSON information about the server and its LiveIP information.
     This will also return the path to the JSON file that was created.

    Args:
        serverNumber (str): '02' This is the server number as it shows up in the sheets.
            IF the sheets are as '2' then you need to pass that. This is a known limitation of
            the code.
        liveIPSourceFile (str): Path to the CSV file that is the export of the worksheets
            Multicast IP A-UNIT.

    Returns:
        string : Path to the JSON file that was created.
        dict : The JSON data that was created.
    """
    logger.info(f"Loading LiveIP JSON for Server Number {serverIP}")
    serverNumber = "{:02}".format(serverIP[-2:])
    dataHand = open(liveIPSourceFile, "r")

    # Sucessfully loaded the spreadsheet into Data read as [row][column]
    dataRead = csv.reader(dataHand.readlines())
    dataRead = list(dataRead)

    # Debug to print out the CSV and the length of it.
    if DEBUG:
        length = 0
        for row in dataRead:
            # if DEBUG: print(row)
            length += 1
        # if DEBUG: print(length)

    # Find the rows that start with EVS.
    deviceName: str = "EVS " + serverNumber
    headers = [x.strip().replace("\n", "") for x in dataRead[0]]

    # Sets a bunch of the header information so we can access it.
    rtr_nameIndex = headers.index("RTR_NAME")
    rtr_nameName = headers[rtr_nameIndex].replace("\\n", "")
    port_or_connectorIndex = headers.index("PORT_OR_CONNECTOR")
    port_or_connectorName = headers[port_or_connectorIndex].replace("\\n", "")
    directionIndex = headers.index("DIRECTION")
    directionName = headers[directionIndex].replace("\\n", "")
    udpPortIndex = headers.index("UDP_PORT")
    udpPortName = headers[udpPortIndex].replace("\\n", "")
    videoIndex = headers.index("VIDEO_\\nPURPLE")
    videoName = headers[videoIndex].replace("\\n", "")
    audioG1Index = headers.index("AUDIO_G1_\\nPURPLE")
    audioG1Name = headers[audioG1Index].replace("\\n", "")
    audioG2Index = headers.index("AUDIO_G2_\\nPURPLE")
    audioG2Name = headers[audioG2Index].replace("\\n", "")
    ancIndex = headers.index("ANC_\\nPURPLE")
    ancName = headers[ancIndex].replace("\\n", "")

    if DEBUG:
        print(headers)

    result = {}
    for i, row in enumerate(dataRead[1:]):
        # print(row)
        if row[0] == deviceName.upper():
            # print(f"Row Found: {row}")

            # Found the Device Requested
            startIndex = i
            endIndex = i + 80  # Hardcoded Value
            # We now need to find the lower limit.

            for j, ipRow in enumerate(dataRead[startIndex - 1 : endIndex]):
                # This checks if there is not enough data in the row. Some rows do not include
                # multicast information.
                # if len(ipRow) < 18:
                #     continue
                # If the row is not captured in result.keys(), we will build it as equal to a
                # blank dictionary.
                if ipRow[directionIndex] not in result.keys():
                    result[ipRow[directionIndex]] = {}
                if DEBUG:
                    print(result.keys())
                if len(ipRow) < ancIndex:
                    ipRow.extend(["" for i in range(ancIndex - len(ipRow)+1)])
                # This we set the keys and values to the result.
                ipRow[rtr_nameIndex] = ipRow[rtr_nameIndex].strip()
                result[ipRow[directionIndex]][ipRow[rtr_nameIndex]] = {
                    videoName: ipRow[videoIndex],
                    audioG1Name: ipRow[audioG1Index],
                    audioG2Name: ipRow[audioG2Index],
                    ancName: ipRow[ancIndex],
                    udpPortName: ipRow[udpPortIndex],
                }
    logger.info(f"Found {len(result.keys())} Records")
    if "TX" in result.keys():
        logger.info(f"Found {len(result['TX'].keys())} TX Records")
    if "RX" in result.keys():
        logger.info(f"Found {len(result['RX'].keys())} RX Records")

    # json.dump(result, open(dest_path, "w"))

    # logger.info(f"Wrote {outPutFilePath}")

    return result


def buildLiveIPcsv(
    serverIP: str,
    numIn: int,
    numOut: int,
    slsm1: str,
    slsm2: str,
    slsm1spd: str,
    slsm2spd: str,
    output: str = None,
    version: str = None,
    workSheetData: dict = None,
) -> list[list]:
    """This builds the CSV file that is used to configure the LiveIP. This is what you could upload
     to the server.

    Args:
        serverNumber (int): as an integer the truck number of the server.
        numIn (int): Number of inputs
        numOut (int): Number of outputs
        output (str): output file path
        version (str): What version the server is running
        workSheetData (dict): Data from the worksheets, the IP information. This is the JSON file
            that was created.

    Returns:
        str: Output file path if successful.
    """
    serverNumber = "{:02}".format(serverIP[-2:])
    logger.info(f"Building LiveIP CSV for Server Number {serverNumber}")


    finalResult = []
    resultHeader = [
        "Version",
        "Field rate",
        "Inputs",
        "Outputs",
        "SLSM #1",
        "SLSM #2",
        "SLSM Speed #1",
        "SLSM Speed #2",
        "XHub-Via",
        "2022-7",
        "Fill and Key",
    ]
    resultHeaderData = [
        version,
        "59.94",
        numIn,
        numOut,
        slsm1,
        slsm2,
        slsm1spd,
        slsm2spd,
        "X",
        "",
        "",
        "",
    ]
    finalResult.append(resultHeader)
    finalResult.append(resultHeaderData)

    # Build Vido IN Array
    def buildVideoIn():
        logger.info("Building Video IN Array")
        array = []
        title = ["Video", "IN"]
        header = [
            "Label",
            "Primary/Secondary",
            "Enabled stream",
            "Enabled Source Address",
            "Source Address",
            "Enabled Source Port",
            "Source Port",
            "Destination Address",
            "Destination Port",
            "SFP",
        ]
        array.append(title)
        array.append(header)
        numIter = numIn
        if slsm1 != "0":
            numIter = numIter + (int(slsm1) * int(slsm1spd.replace("x", "")) - 1)

        if slsm2 != "0":
            numIter = numIter + (int(slsm2) * int(slsm2spd.replace("x", "")) - 1)
        if slsm1 == "0" and slsm2 == "0":
            numIter += 1
        i = 1
        for x in range(1, numIter):
            if slsm1 == "0" or (i > int(slsm1)):
                if slsm1 == "0":
                    x = i
                tempLine = [
                    f"IN{x} Video",
                    "PRI",
                    "X",
                    "",
                    "192.168.0.1",
                    "",
                    30000,
                    "239.1.1.1",
                    30000,
                    "C",
                ]
            else:
                j = x % int(slsm1spd.replace("x", ""))
                if j == 0:
                    j = int(slsm1spd.replace("x", ""))
                # print(f"i: {i}, j: {j}")
                tempLine = [
                    f"IN{i} PHASE-{j}",
                    "PRI",
                    "X",
                    "",
                    "192.168.0.1",
                    "",
                    30000,
                    "239.1.1.1",
                    30000,
                    "C",
                ]
                if j == int(slsm1spd.replace("x", "")):
                    i += 1
            array.append(tempLine)

        if DEBUG:
            print(array)
        return array

    def buildVideoOut():
        logger.info("Building Video OUT Array")
        array = []
        title = ["Video", "OUT"]
        header = [
            "Label",
            "Primary/Secondary",
            "Enabled stream",
            "Source Port",
            "Destination Address",
            "Destination Port",
            "SFP",
        ]
        array.append(title)
        array.append(header)
        for x in range(1, numOut + 1):
            x2 = "{:02}".format(x)
            tempLine = [
                f"OUT{x} Video",
                "PRI",
                "X",
                workSheetData["TX"][f"CLEAN OUT {x2}"]["UDP_PORT"],
                workSheetData["TX"][f"CLEAN OUT {x2}"]["VIDEO_PURPLE"],
                workSheetData["TX"][f"CLEAN OUT {x2}"]["UDP_PORT"],
                "C",
            ]
            array.append(tempLine)

        if DEBUG:
            print(array)
        return array

    def buildAudioIn():
        logger.info("Building Audio IN Array")
        array = []
        title = ["Audio", "IN"]
        header = [
            "Label",
            "Primary/Secondary",
            "Enabled stream",
            "Enabled Source Address",
            "Source Address",
            "Enabled Source Port",
            "Source Port",
            "Destination Address",
            "Destination Port",
            "SFP",
            "Audio Type",
            "Channel Grouping",
            "Number of channels",
        ]
        array.append(title)
        array.append(header)
        for x in range(1, numIn + 1):
            for y in range(1, 5):
                if y > 2:
                    enabled = ""
                else:
                    enabled = "X"

                x2 = "{:02}".format(x)
                tempLine = [
                    f"IN{x} Audio-{y}",
                    "PRI",
                    enabled,
                    "",
                    "192.168.0.1",
                    "",
                    30000,
                    "239.1.1.1",
                    30000,
                    "C",
                    "ST 2110-30",
                    "",
                    8,
                ]
                array.append(tempLine)

        if DEBUG:
            print(array)
        return array

    def buildAudioOut():
        logger.info("Building Audio OUT Array")
        array = []
        title = ["Audio", "OUT"]
        header = [
            "Label",
            "Primary/Secondary",
            "Enabled stream",
            "Source Port",
            "Destination Address",
            "Destination Port",
            "SFP",
            "Audio Type",
            "Channel Grouping",
            "Number of channels",
        ]
        array.append(title)
        array.append(header)
        for x in range(1, numOut + 1):
            x2 = "{:02}".format(x)
            for y in range(1, 5):
                if y > 2:
                    enabled = ""
                    udpPort = "30000"
                    ipAddr = "239.1.1.1"
                else:
                    enabled = "X"
                    udpPort = workSheetData["TX"][f"CLEAN OUT {x2}"]["UDP_PORT"]
                    ipAddr = workSheetData["TX"][f"CLEAN OUT {x2}"][f"AUDIO_G{y}_PURPLE"]

                x2 = "{:02}".format(x)
                tempLine = [
                    f"OUT{x} Audio-{y}",
                    "PRI",
                    enabled,
                    udpPort,
                    ipAddr,
                    udpPort,
                    "C",
                    "ST 2110-30",
                    "",
                    8,
                ]
                array.append(tempLine)

        if DEBUG:
            print(array)
        return array

    def buildAncIn():
        logger.info("Building Ancillary IN Array")
        array = []
        title = ["Ancillary", "IN"]
        header = [
            "Label",
            "Primary/Secondary",
            "Enabled stream",
            "Enabled Source Address",
            "Source Address",
            "Enabled Source Port",
            "Source Port",
            "Destination Address",
            "Destination Port",
            "SFP",
        ]
        array.append(title)
        array.append(header)
        for x in range(1, numIn + 1):
            tempLine = [
                f"IN{x} Anc-1",
                "PRI",
                "X",
                "",
                "192.168.0.1",
                "",
                30000,
                "239.1.1.1",
                30000,
                "C",
            ]
            array.append(tempLine)

        if DEBUG:
            print(array)
        return array

    def buildAncOut():
        logger.info("Building Ancillary OUT Array")
        array = []
        title = ["Ancillary", "OUT"]
        header = [
            "Label",
            "Primary/Secondary",
            "Enabled stream",
            "Source Port",
            "Destination Address",
            "Destination Port",
            "Content",
            "SFP",
        ]
        array.append(title)
        array.append(header)
        for x in range(1, numOut + 1):
            x2 = "{:02}".format(x)
            tempLine = [
                f"OUT{x} Anc-1",
                "PRI",
                "X",
                workSheetData["TX"][f"CLEAN OUT {x2}"]["UDP_PORT"],
                workSheetData["TX"][f"CLEAN OUT {x2}"]["ANC_PURPLE"],
                workSheetData["TX"][f"CLEAN OUT {x2}"]["UDP_PORT"],
                "334M",
                "C",
            ]
            array.append(tempLine)

        if DEBUG:
            print(array)
        return array

    def buildMonRECOut():
        logger.info("Building Monitoring REC OUT Array")
        array = []
        title = ["Monitoring REC", "OUT"]
        header = [
            "Label",
            "Primary/Secondary",
            "Enabled stream",
            "Source Port",
            "Destination Address",
            "Destination Port",
            "SFP",
        ]
        array.append(title)
        array.append(header)
        for x in range(1, numIn + 1):
            x2 = "{:02}".format(x)
            tempLine = [
                f"MON IN{x} Video",
                "PRI",
                "X",
                workSheetData["TX"][f"MON IN {x2}"]["UDP_PORT"],
                workSheetData["TX"][f"MON IN {x2}"]["VIDEO_PURPLE"],
                workSheetData["TX"][f"MON IN {x2}"]["UDP_PORT"],
                "C",
            ]
            array.append(tempLine)

        if DEBUG:
            print(array)
        return array

    def buildMonPGMOut():
        logger.info("Building Monitoring PGM OUT Array")
        array = []
        title = ["Monitoring PGM", "OUT"]
        header = [
            "Label",
            "Primary/Secondary",
            "Enabled stream",
            "Source Port",
            "Destination Address",
            "Destination Port",
            "SFP",
        ]
        array.append(title)
        array.append(header)
        for x in range(1, numOut + 1):
            x2 = "{:02}".format(x)
            tempLine = [
                f"MON OUT{x} Video",
                "PRI",
                "X",
                workSheetData["TX"][f"MON OUT {x2}"]["UDP_PORT"],
                workSheetData["TX"][f"MON OUT {x2}"]["VIDEO_PURPLE"],
                workSheetData["TX"][f"MON OUT {x2}"]["UDP_PORT"],
                "C",
            ]
            array.append(tempLine)

        if DEBUG:
            print(array)
        return array

    def buildMonAudioOut():
        logger.info("Building Monitoring Audio OUT Array")
        array = []
        title = ["Audio Monitoring", "OUT"]
        header = [
            "Label",
            "Primary/Secondary",
            "Enabled stream",
            "Source Port",
            "Destination Address",
            "Destination Port",
            "SFP",
            "Audio Type",
            "Channel Grouping",
            "Number of channels",
        ]
        array.append(title)
        array.append(header)
        for x in range(1, numIn + 1):
            x2 = "{:02}".format(x)
            for y in range(1, 5):
                if y > 2:
                    enabled = ""
                    udpPort = "30000"
                    ipAddr = "239.1.1.1"
                else:
                    enabled = "X"
                    udpPort = workSheetData["TX"][f"MON IN {x2}"]["UDP_PORT"]
                    ipAddr = workSheetData["TX"][f"MON IN {x2}"][f"AUDIO_G{y}_PURPLE"]

                x2 = "{:02}".format(x)
                tempLine = [
                    f"MON IN{x} Audio-{y}",
                    "PRI",
                    enabled,
                    udpPort,
                    ipAddr,
                    udpPort,
                    "C",
                    "ST 2110-30",
                    "",
                    8,
                ]
                array.append(tempLine)

        if DEBUG:
            print(array)
        return array

    def buildMVVideoIn():
        logger.info("Building Multiviewer Video IN Array")
        array = []
        title = ["Multiviewer", "IN"]
        header = [
            "Label",
            "Primary/Secondary",
            "Enabled stream",
            "Enabled Source Address",
            "Source Address",
            "Enabled Source Port",
            "Source Port",
            "Destination Address",
            "Destination Port",
            "SFP",
        ]
        array.append(title)
        array.append(header)
        for x in range(1, 3):
            tempLine = [
                f"MV IN{x} Video",
                "PRI",
                "X",
                "",
                "192.168.0.1",
                "",
                30000,
                "239.1.1.1",
                30000,
                "C",
            ]
            array.append(tempLine)

        if DEBUG:
            print(array)
        return array

    def buildMVVideoOut():
        logger.info("Building Multiviewer Video OUT Array")
        array = []
        title = ["Multiviewer", "OUT"]
        header = [
            "Label",
            "Primary/Secondary",
            "Enabled stream",
            "Source Port",
            "Destination Address",
            "Destination Port",
            "SFP",
        ]
        array.append(title)
        array.append(header)
        for x in range(1, 5):
            x2 = "{:02}".format(x)
            tempLine = [
                f"MV OUT{x} Video",
                "PRI",
                "X",
                workSheetData["TX"][f"MV OUT {x2}"]["UDP_PORT"],
                workSheetData["TX"][f"MV OUT {x2}"]["VIDEO_PURPLE"],
                workSheetData["TX"][f"MV OUT {x2}"]["UDP_PORT"],
                "C",
            ]
            array.append(tempLine)

        if DEBUG:
            print(array)
        return array

    #####
    #
    # Builds the sheet here
    #
    ####
    finalResult.append([""])
    finalResult += buildVideoIn()
    finalResult.append([""])
    finalResult += buildVideoOut()
    finalResult.append([""])
    finalResult += buildAudioIn()
    finalResult.append([""])
    finalResult += buildAudioOut()
    finalResult.append([""])
    finalResult += buildAncIn()
    finalResult.append([""])
    finalResult += buildAncOut()
    finalResult.append([""])
    finalResult += buildMonRECOut()
    finalResult.append([])
    finalResult += buildMonPGMOut()
    finalResult.append([])
    finalResult += buildMonAudioOut()
    finalResult.append([""])
    finalResult += buildMVVideoIn()
    finalResult.append([""])
    finalResult += buildMVVideoOut()
    finalResult.append([""])

    logger.info(f"Built CSV with {len(finalResult)} rows")

    if DEBUG:
        for row in finalResult:
            print(row)

    return finalResult


def getconfigLineData(
    serverIP: str,
    version: str,
    worksheetData: dict,
    configLineNumber: int = None,
):
    serverNum = re.match("^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$", serverIP)[1]
    logger.info(f"Fetching Config Line Data for  {serverNum}")
    if DEBUG:
        print(serverNum)

    if configLineNumber is None:
        numIter = range(1, 17)
    elif isinstance(configLineNumber, int):
        numIter = [configLineNumber]

    for i in tqdm.tqdm(numIter):
        params = {
            "SessionID": "Reset",
            "NumLine": i,
            "Meta": "true",
            "Reset": "false",
            "All": "true",
        }
        reqData = requests.get(
            f"http://{serverIP}/cfgweb/CfgWeb.dll/GetConfigValuesJS",
            params=params,
        )
        reqJson = reqData.json()
        numIn = reqJson["CFG_PARAM_NB_RECORDER"]["Value"]
        numOut = reqJson["CFG_PARAM_NB_PLAYER"]["Value"]
        slsm1 = reqJson["CFG_PARAM_SLSM_REC_CAMERA_COUNT"]["Text"]
        slsm2 = reqJson["CFG_PARAM_SECOND_SLSM_REC_CAMERA_COUNT"]["Text"]
        slsm1spd = reqJson["CFG_PARAM_SLSM_REC_SPEED"]["Text"]
        slsm2spd = reqJson["CFG_PARAM_SECOND_SLSM_REC_SPEED"]["Text"]
        logger.info(f"Num In: {numIn} Num Out: {numOut}")
        # print(reqJson)
        if DEBUG:
            print(f"Building Live IPs for {i}")

        buildLiveIPcsv(
            serverNumber=serverNum,
            numIn=numIn,
            numOut=numOut,
            slsm1=slsm1,
            slsm2=slsm2,
            slsm1spd=slsm1spd,
            slsm2spd=slsm2spd,
            output=f"../../../../tmp/{serverNum}LiveIPCFG{i}.csv",
            version=version,
            workSheetData=worksheetData,
        )


def sendLiveIPs(serverIP: str, configLineNumber: int = None):
    serverNum = re.match("^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$", serverIP)[1]

    def getSessionID() -> requests.Response:
        # Get our SessionID to Use for this block of requests.
        logger.info(f"Getting SessionID for {serverIP}")
        params = {
            "SessionID": "Reset",
            "NumLine": 1,
            "Meta": "true",
            "Reset": "false",
            "All": "true",
        }
        r = requests.get(
            f"http://{serverIP}/ipconfigurationweb/setlinenumberactionjs",
            params=params,
        )
        sessionID = r.json()["SessionID"]
        return sessionID

    def setLineNumber(lineNum: int = 1, sessionID: str = "Reset") -> requests.Response:
        # Emulates we then set the line number again, just to make sure.
        logger.info(f"Setting Line Number to {lineNum} for {serverIP}")
        params = {"SessionID": sessionID, "number": lineNum}
        r = requests.get(
            f"http://{serverIP}/ipconfigurationweb/setlinenumberactionjs",
            params=params,
        )
        return r.json()

    def sendCSV(path: str, sessionID: str) -> requests.Response:
        # Emulates Sending the CSV File
        logger.info(f"Sending CSV File for {serverIP}")
        with open(path, "rb") as cfgHand:
            r = requests.post(
                f"http://{ serverIP }/ipconfigurationweb/importcsvactionjs?SessionId={sessionID}",
                files={"ConfigFile": cfgHand},
            )
        print(r.text)
        return r

    def commit(sessionID: str) -> requests.Response:
        # Commits, in theory no changes though as the importcsvaction is setting all the parameters for us.
        logger.info(f"Committing changes for {serverIP}")
        r = requests.get(
            f"http://{ serverIP }/ipconfigurationweb/commitactionjs?SessionId={sessionID}",
        )
        return r

    def setURI(uri: str, value: str, sessionID: str = "Reset") -> requests.Response:
        # Sets a URI to a value
        logger.info(f"Setting {uri} to {value} for {serverIP}")
        r = requests.post(
            f"http://{serverIP}/ipconfigurationweb/setparametervalueactionjs?SessionId={sessionID}",
            data={"uri": uri, "value": value},
        )
        return r

    def setPTP(ptpDomain: str = "127", sessionID: str = "Reset") -> requests.Response:
        # Sets PTP to 127
        logger.info(f"Setting PTP Domain to {ptpDomain} for {serverIP}")
        r = setURI("/liveip/ptp/domain", ptpDomain, sessionID)
        return r

    def setAES67(audioTiming: str = "125", sessionID: str = "Reset") -> requests.Response:
        # Sets AES67 Packet Time to 125
        logger.info(f"Setting AES67 Packet Time to {audioTiming} for {serverIP}")
        r = setURI("/liveip/aes67/packettime", audioTiming, sessionID)
        return r

    def setNMOSVersion(sessionID: str = "Reset") -> requests.Response:
        # Hard coded sets NMOS to 1.3
        logger.info(f"Setting NMOS Version to 1.3 for {serverIP}")
        r = setURI("/liveip/protocol/NMOSrdsVersion", "3", sessionID)
        return r

    def needToBeUpdated(sessionID: str = "Reset") -> requests.Response:
        # Sets AES67 Packet Time to 125
        logger.info(f"Checking if {serverIP} needs to be updated")
        r = requests.get(
            f"http://{serverIP}/ipconfigurationweb/needtobeupdatedactionjs?SessionId={sessionID}",
        )
        return r

    # This handles setting the numIter which is what is itterated over, so if it is None, we set it to 1-16,
    # otherwise we set it to an list.
    if configLineNumber is None:
        numIter = range(1, 17)
    elif isinstance(configLineNumber, int):
        numIter = [configLineNumber]

    """
    This is the master Loop, this will set send all the LiveIPs based on the iterable that is
    passed into tqdm.
    This will set the working line number and then send the CSV file to the server.
    This will also set the PTP Domain to 127 and the AES67 Packet Time to 125.
    """
    logger.info(f"Itterating over {numIter}")
    for i in tqdm.tqdm(numIter):
        cfgPath = f"../../../../tmp/{serverNum}LiveIPCFG{i}.csv"

        print(f"Sending IP: {serverIP}, cfg line {i}")
        print(cfgPath)

        sessionID = getSessionID()
        setLineNumber(i, sessionID)
        # setNMOSVersion(sessionID)
        # commit(sessionID)
        sendCSV(cfgPath, sessionID)
        commit(sessionID)
        setPTP("127", sessionID)
        commit(sessionID)
        setAES67("125", sessionID)
        commit(sessionID)
        needToBeUpdated(sessionID)
    logger.info(f"Finished sending Live IPs for {serverIP}")


def worker(serverIP: str, configLineNumber: int, mcVersion: str, operation: str) -> None:

    if operation == "build":
        (serverIPDataPath, serverIPData) = loadIPJson(
            serverIP=serverIP,
            liveIPSourceFile="./tmp/FLAGSHIP_ABC_4K_WORKSHEETS - NETWORK MULTICAST IP A-UNIT.csv",
        )
        getconfigLineData(
            serverIP=serverIP,
            version=mcVersion,
            worksheetData=serverIPData,
            configLineNumber=configLineNumber,
        )
    elif operation == "send":
        sendLiveIPs(
            serverIP=serverIP,
            configLineNumber=configLineNumber,
        )
    elif operation == "buildSend":
        (serverIPDataPath, serverIPData) = loadIPJson(
            serverIP=serverIP,
            liveIPSourceFile="./tmp/FLAGSHIP_ABC_4K_WORKSHEETS - NETWORK MULTICAST IP A-UNIT.csv",
        )
        getconfigLineData(
            serverIP=serverIP,
            version=mcVersion,
            worksheetData=serverIPData,
            configLineNumber=configLineNumber,
        )
        sendLiveIPs(
            serverIP=serverIP,
            configLineNumber=configLineNumber,
        )
    else:
        print("Invalid operation")
        exit(1)


def main():
    parser = argparse.ArgumentParser(description="This will make Live IPs for all 16 Config Lines")
    parser.add_argument("--serverIP", type=str, help="EVS Server IP", required=True)
    parser.add_argument("--configLineNumber", type=int, help="Config Line Number", required=False)
    parser.add_argument("--mcVersion", type=str, help="Multicam Version", required=False)
    parser.add_argument(
        "--operation",
        type=str,
        help="Operation, options are [build, send, buildSend]",
        required=False,
    )

    args = parser.parse_args()

    if args.operation == "build":
        (serverIPDataPath, serverIPData) = loadIPJson(
            serverIP=args.serverIP,
            liveIPSourceFile="./tmp/FLAGSHIP_ABC_4K_WORKSHEETS - NETWORK MULTICAST IP A-UNIT.csv",
        )
        getconfigLineData(
            serverIP=args.serverIP,
            version=args.mcVersion,
            worksheetData=serverIPData,
            configLineNumber=args.configLineNumber,
        )
    elif args.operation == "send":
        sendLiveIPs(
            serverIP=args.serverIP,
            configLineNumber=args.configLineNumber,
        )
    elif args.operation == "buildSend":
        (serverIPDataPath, serverIPData) = loadIPJson(
            serverIP=args.serverIP,
            liveIPSourceFile="./tmp/FLAGSHIP_ABC_4K_WORKSHEETS - NETWORK MULTICAST IP A-UNIT.csv",
        )
        getconfigLineData(
            serverIP=args.serverIP,
            version=args.mcVersion,
            worksheetData=serverIPData,
            configLineNumber=args.configLineNumber,
        )
        sendLiveIPs(
            serverIP=args.serverIP,
            configLineNumber=args.configLineNumber,
        )
    else:
        print("Invalid operation")
        exit(1)


def dev():
    data = loadIPJson("01", "./PRIMEONE_4K_WORKSHEETS - MULTICAST IP.csv")
    buildLiveIPcsv(
        serverNumber="01",
        numIn=10,
        numOut=2,
        slsm1=0,
        slsm2=0,
        slsm1spd="2x",
        slsm2spd="2x",
        output=f"../../../../tmp/01LiveIPCFG1.csv",
        version="20.7.35",
        redundancy=True,
        workSheetData=data,
    )


if __name__ == "__main__":
    # loadIPJson("01")
    # buildLiveIP(1, 8, 4)
    main()
    # dev()
```