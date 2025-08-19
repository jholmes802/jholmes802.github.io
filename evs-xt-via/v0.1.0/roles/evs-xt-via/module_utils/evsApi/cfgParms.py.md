# cfgParms.py
```python
from __future__ import annotations
from typing import Any
import tqdm
import ipaddress
import re
import logging

logger = logging.getLogger(__name__)


class configParamRaw:
    def __init__(self, data: dict, updateFunc: function = None, readFunc: function = None) -> None:
        """Config Parameter Raw Class, this only applies to a couple of parameters but it is useful.

        Args:
            data (dict): Config Parameter Data
            updateFunc (function, optional): The function to be called when updating the value of the parameter. Not applicable for configParamRaw. Defaults to None.
            readFunc (function, optional): The function to be called when reading/refreshing the value of the parameter. Defaults to None.
        """
        self._data: dict = data
        self._updateFunc: function = updateFunc  # Writes to the server
        self._readFunc: function = readFunc  # Reads from the server

    def getType(self) -> str:
        return self._data["Type"]

    def getParamName(self) -> str:
        return self._data["ParamName"]

    def getParamID(self) -> int:
        return self._data["ParamID"]

    def getRequiresReboot(self) -> bool:
        return self._data["Reboot"]

    def __str__(self) -> str:
        return f"Name: {self.getParamName()} | Type: {self.getType()}"

    def data(self) -> dict:
        return self._data


class configParamBase(configParamRaw):
    def __init__(self, data: dict, updateFunc: function = None, readFunc: function = None) -> None:
        """This function extends the configParamRaw class and adds the ability for values to be set and read.

        Args:
            data (dict): Config Parameter Data
            updateFunc (function, optional): Update Function to be called when needed. Defaults to None.
            readFunc (function, optional): Read Function to be called when refreshing the data. Defaults to None.
        """
        super().__init__(data, updateFunc=updateFunc, readFunc=readFunc)

    def getCurrentValue(self) -> Any:
        return self._data["CurrentValue"]

    def setCurrentValue(self, value: Any) -> None:
        """Sets the CurrentValue with one attempt to rety it, this allows us to

        Args:
            value (Any): Value you want to set this parameter to.
        """
        # We call the server asking for it to update the value.

        self._updateFunc(self.getParamName(), value)

        # This reads the value to see if it was updated.
        temp = self._readFunc(self.getParamName())

        # If the value has not been updated we try again.
        if temp["CurrentValue"] != value:
            logger.warning(f"Unable to set {self.getParamName()} to {value} trying again")
            self._updateFunc(self.getParamName(), value)

        # Then we update the current Value
        self._data = temp

    def getCurrentLabel(self) -> str:
        return self._data["CurrentLabel"]

    def setCurrentLabel(self, value: str) -> None:
        self._data["CurrentLabel"] = value

    def getDefaultValue(self) -> Any:
        return self._data["Default"]

    def getMaxValue(self) -> int:
        return self._data["MaxValue"]

    def __str__(self) -> str:
        return f"Name: {self.getParamName()} | Value: {self.getCurrentValue()} | Label: {self.getCurrentLabel()} | Type: {self.getType()}"


class configParamNumeric(configParamBase):
    def __init__(self, data: dict, updateFunc: function = None, readFunc: function = None) -> None:
        super().__init__(data, updateFunc=updateFunc, readFunc=readFunc)

    def setCurrentValue(self, value):
        # This also handles setting the appropriate label.

        # Going to implment checks to ensure its within the bounds.
        if value > self.getMaxValue():
            value = self.getMaxValue()

        elif value < self.getMinValue():
            value = self.getMinValue()

        super().setCurrentValue(value)
        super().setCurrentLabel(str(value))

    def getMinValue(self) -> int:
        return self._data["MinValue"]


class configParamSelection(configParamNumeric):
    def __init__(self, data: dict, updateFunc: function = None, readFunc: function = None) -> None:
        super().__init__(data, updateFunc=updateFunc, readFunc=readFunc)

    def getValuesVals(self) -> list[dict]:
        returnable = []
        for i in self.getValues():
            returnable.append(i["Value"])
        return returnable

    def getValuesLabels(self) -> list[str]:
        returnable = []
        for i in self.getValues():
            returnable.append(i["Label"])
        return returnable

    def getAllOptions(self) -> list:
        returnable = self.getValuesVals() + self.getValuesLabels()
        return returnable

    def getValues(self) -> list[dict]:
        return self._data["Values"]

    def getValue(self, val: int = None, label: str = None) -> dict:
        if val is None and label is None:
            raise ValueError("Must provide either a value or label.")
        elif val is not None:
            for i in self.getValues():
                if i["Value"] == val:
                    return i
        elif label is not None:
            for i in self.getValues():
                if i["Label"] == label:
                    return i
        raise ValueError("Value not found.")

    def setCurrentValue(self, value: Any) -> None:
        """This is for ones that are selection based, there are options, such as 1080P which needs to be converted to the appropriate value.

        Args:
            value (Any): The Value, can be the new label or the value, this will convert.

        Raises:
            ValueError: If it cannot find the Value in the list of possible it will error out.
        """
        if value not in self.getAllOptions():
            raise ValueError(f"Value {value} is not in the list of values.")
        # This block finds out if the user is setting the direct int or a label.
        if value in self.getValuesLabels():
            valueDict: dict = self.getValue(label=value)
        elif value in self.getValuesVals():
            valueDict: dict = self.getValue(val=value)
        else:
            raise ValueError(f"Value {value} is not in the list of values.")

        super().setCurrentValue(valueDict["Value"])
        super().setCurrentLabel(valueDict["Label"])


class configParamString(configParamBase):
    def __init__(self, data: dict, updateFunc: function = None, readFunc: function = None) -> None:
        super().__init__(data, updateFunc=updateFunc, readFunc=readFunc)

    def getCurrentLabel(self) -> str:
        return super().getCurrentLabel()

    def getCurrentValue(self) -> str:
        return super().getCurrentValue()

    def setCurrentValue(self, value: str):
        if len(value) > self.getMaxValue():
            raise ValueError(f"Value {value} is too long.")
        super().setCurrentValue(value)
        super().setCurrentLabel(value)


class configParamIP(configParamBase):
    def __init__(self, data: dict, updateFunc: function = None, readFunc: function = None) -> None:
        super().__init__(data, updateFunc=updateFunc, readFunc=readFunc)

    def getCurrentLabel(self) -> int:
        ip_int = super().getCurrentValue()
        ip_str = str(ipaddress.ip_address(ip_int))
        return re.sub("^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})$", r"\4.\3.\2.\1", ip_str)

    def setCurrentValue(self, value: str):
        if value.count(".") != 3:
            raise ValueError(f"Value {value} is not a valid IP address.")

        ip_int = int(
            ipaddress.ip_address(
                re.sub("^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})$", r"\4.\3.\2.\1", value)
            )
        )

        super().setCurrentValue(ip_int)
        super().setCurrentLabel(value.replace(".", ""))


class configLine:
    def __init__(
        self,
        numLine: int,
        readFunc: function = None,
        updateFunc: function = None,
        readParam: function = None,
        singleParam: str = None,
    ) -> None:
        self._numLine: int = numLine
        self._data: dict[str, configParamBase] = None
        self._updateFunc: function = updateFunc
        self._readFunc: function = readFunc
        self._readParam: function = readParam
        if self._data is None and singleParam is None:
            self._buildMe()
        elif self._data is None and singleParam is not None:
            self._data = {}
            self._buildParam(singleParam)

    def _refreshAll(self):
        newData: dict = self._readFunc(self._numLine)
        print(newData)

    def _buildMe(self):
        wholeLine: dict[str] = self._readFunc(self._numLine)
        self._data = {}

        remove = [
            "SessionID",
            "IsMulticamRunning",
            "IsMulsetupRunning",
            "IsBootWinsRunning",
            "IsTechnicalLocked",
            "HasSharedConfigChanged",
            "SharedNumLineLoaded",
        ]

        for i in [x for x in wholeLine.keys() if x.startswith("DEPRECATED")]:
            wholeLine.pop(i)

        for i in [x for x in wholeLine.keys() if x.startswith("SNMP")]:
            wholeLine.pop(i)

        for i in remove:
            wholeLine.pop(i)

        for k, v in tqdm.tqdm(wholeLine.items()):
            self._buildParam(k)

    def _buildParam(self, paramName: str):
        desc: dict = self._readParam(paramName, self._numLine)
        if "Error" in desc.keys():
            # logger.debug(f"Unable to Fetch info about {paramName} | Error: {desc['Error']}")
            return None
        elif "Type" not in desc.keys():
            if "Values" in desc.keys():
                result = configParamSelection(desc, updateFunc=self._updateMiddleware, readFunc=self._readMiddleware)
        elif desc["Type"] == "numeric":
            if "Values" in desc.keys():
                if desc["MaxValue"] == -1:
                    result = configParamIP(desc, updateFunc=self._updateMiddleware, readFunc=self._readMiddleware)
                else:
                    result = configParamSelection(
                        desc, updateFunc=self._updateMiddleware, readFunc=self._readMiddleware
                    )
            else:
                result = configParamNumeric(desc, updateFunc=self._updateMiddleware, readFunc=self._readMiddleware)
        elif desc["Type"] == "char":
            result = configParamString(desc, updateFunc=self._updateMiddleware, readFunc=self._readMiddleware)
        elif desc["Type"] == "raw":
            result = configParamRaw(desc, updateFunc=self._updateMiddleware, readFunc=self._readMiddleware)
        else:
            # logger.debug(f"Unknown Param Type {desc['Type']} | {desc}")
            raise Exception(f"Unknown Param Type {desc['Type']}")
        self._data[paramName] = result

    def _updateMiddleware(self, paramName: str, value: Any):
        return self._updateFunc(self._numLine, paramName, value, True)

    def _readMiddleware(self, paramName: str):
        return self._readParam(paramName, self._numLine)

    def get_param(self, paramName: str) -> configParamBase:
        return self._data[paramName]

    def data(self):
        result = {"numLine": self._numLine, "data": {k: v.data() for k, v in self._data.items()}} {% endraw %}
        return result


if __name__ == "__main__":
    test = {
        "ParamName": "CFG_PARAM_SLSM_REC_CAMERA_COUNT",
        "ParamID": 22426,
        "Reboot": True,
        "Type": "numeric",
        "Default": 0,
        "MaxValue": 8,
        "CurrentValue": 0,
        "CurrentLabel": "0",
        "MinValue": 0,
    }

    numTest = configParamNumeric(test)
    print(numTest)
```