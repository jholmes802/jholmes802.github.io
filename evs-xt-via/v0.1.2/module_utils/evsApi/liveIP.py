from __future__ import annotations
import json
from typing import Any


class LiveIPBase:
    def __init__(self, data: dict, updateFunc, readFunc) -> None:
        self._data: dict = data
        self._uri: str = self.data()["uri"]
        self._visible: bool = self.getMetadata()["Visibility"]
        self._editable: bool = self.getMetadata()["Editable"]
        self._IsReboot: bool = self.getMetadata()["IsReboot"]
        self._IsInvalid: bool = self.getMetadata()["IsInValid"]
        self._type: str = data["Type"]
        self._updateFunc: function = updateFunc
        self._readFunc: function = readFunc

    def getMetadata(self) -> dict:
        return self._data["Metadata"]

    def data(self) -> dict:
        return self._data

    def getEditable(self) -> bool:
        return self.getMetadata()["Editable"]

    def getValue(self) -> Any:
        try:
            return self._data["Value"]
        except:
            return None

    def getUri(self) -> str:
        return self._uri

    def setValue(self, value: Any) -> None:
        if not self.getEditable():
            raise Exception("Cannot set value of non-editable field.")

        response = self._updateFunc(self.getUri(), value)

        if "Data" not in response.keys():
            raise Exception(f"Error 1 updating value for URI: {self.getUri()} got error {response}")

        if response["Data"]["SetParameterValue"] != "Success":
            raise Exception(f"Error 2 updating value for URI: {self.getUri()} got error {response}")

        self._data = self._readFunc(self.getUri())


class LiveIPInteger(LiveIPBase):
    def __init__(self, data: dict, updateFunc, readFunc) -> None:
        super().__init__(data, updateFunc, readFunc)
        self._value: int = data["Value"]
        self._min: int = self.getMetadata()["Minimum"]
        self._max: int = self.getMetadata()["Maximum"]

    def setValue(self, value: int) -> None:
        if not self.getEditable():
            raise Exception("Cannot set value of non-editable field.")
        if len(value) > self._max:
            Tvalue = self._max
        elif len(value) < self._min:
            Tvalue = self._min
        else:
            Tvalue = value
        super().setValue(Tvalue)

    def getValue(self) -> int:
        return self._value


class LiveIPEnum(LiveIPBase):
    def __init__(self, data: dict, updateFunc, readFunc) -> None:
        super().__init__(data, updateFunc, readFunc)
        self._value: str = data["Value"]
        self._displayText: str = data["DisplayText"]
        self._values: dict = self.getMetadata()["Values"]

    def setValue(self, value: str) -> None:
        if not self.getEditable():
            raise Exception("Cannot set value of non-editable field.")
        if value not in self._values:
            raise Exception(f"Invalid value: {value}")
        super().setValue(value)
        self._displayText = self._values[value]

    def getValue(self) -> str:
        return self._value


class LiveIPString(LiveIPBase):
    def __init__(self, data: dict, updateFunc, readFunc) -> None:
        super().__init__(data, updateFunc, readFunc)
        self._value: str = data["Value"]
        self._maxLength: int = self.getMetadata()["Maxlenght"]

    def setValue(self, value: str) -> None:
        if not self.getEditable():
            raise Exception("Cannot set value of non-editable field.")
        if len(value) > self._maxLength:
            raise Exception(f"Value too long. Max length is {self._maxLength} characters.")
        super().setValue(value)

    def getValue(self) -> str:
        return self._value


class LiveIPBool(LiveIPBase):
    def __init__(self, data: dict, updateFunc, readFunc) -> None:
        super().__init__(data, updateFunc, readFunc)
        self._value: bool = data["Value"]

    def setValue(self, value: bool) -> None:
        if not self.getEditable():
            raise Exception("Cannot set value of non-editable field.")

        super().setValue(value)

    def getValue(self) -> bool:
        return self._value


class Stream:

    def __init__(self, data: dict, updateFunc, readFunc) -> None:
        self._destinationAddress: LiveIPString = LiveIPString(data["/destinationaddress"], updateFunc, readFunc)
        self._destinationPort: LiveIPInteger = LiveIPInteger(data["/destinationport"], updateFunc, readFunc)
        self._enabled: LiveIPBool = LiveIPBool(data["/enabled"], updateFunc, readFunc)
        self._module: LiveIPInteger = LiveIPInteger(data["/module"], updateFunc, readFunc)
        self._physicalPorts: LiveIPEnum = LiveIPEnum(data["/physicalports"], updateFunc, readFunc)
        self._name: LiveIPString = LiveIPString(data["/name"], updateFunc, readFunc)

    def data(self):
        result = {
            "desinationAddress": self._destinationAddress.data(),
            "destinationPort": self._destinationPort.data(),
            "enabled": self._enabled.data(),
            "module": self._module.data(),
            "physicalPorts": self._physicalPorts.data(),
            "name": self._name.data(),
        }
        return result

    # Getters and Setters for DestinationAddress

    def get_destinationAddress(self) -> str:
        return self._destinationAddress.getValue()

    def get_desinationAddress_raw(self) -> LiveIPString:
        return self._destinationAddress

    def set_destinationAddress(self, value: str) -> None:
        self._destinationAddress.setValue(value)

    # Getters and Setters for DestinationPort

    def get_destinationPort(self) -> int:
        return self._destinationPort.getValue()

    def get_destinationPort_raw(self) -> LiveIPInteger:
        return self._destinationPort

    def set_destinationPort(self, value: int) -> None:
        self._destinationPort.setValue(value)

    # Getters and Setters for Enabled

    def get_enabled(self) -> bool:
        return self._enabled.getValue()

    def get_enabled_raw(self) -> LiveIPBool:
        return self._enabled

    def set_enabled(self, value: bool) -> None:
        self._enabled.setValue(value)

    # Getters and Setters for Module

    def get_module(self) -> int:
        return self._module.getValue()

    def get_module_raw(self) -> LiveIPInteger:
        return self._module

    def set_module(self, value: int) -> None:
        self._module.setValue(value)

    # Getters and Setters for PhysicalPorts

    def get_physicalPorts(self) -> str:
        return self._physicalPorts.getValue()

    def get_physicalPorts_raw(self) -> LiveIPEnum:
        return self._physicalPorts

    def set_physicalPorts(self, value: str) -> None:
        self._physicalPorts.setValue(value)

    # Getters and Setters for Name

    def get_name(self) -> str:
        return self._name.getValue()

    def get_name_raw(self) -> LiveIPString:
        return self._name

    def set_name(self, value: str) -> None:
        self._name.setValue(value)


class OutputStream(Stream):
    def __init__(self, data: dict, updateFunc, readFunc) -> None:
        super().__init__(data, updateFunc, readFunc)


class InputStream(Stream):
    def __init__(self, data: dict, updateFunc: function, readFunc: function) -> None:
        super().__init__(data, updateFunc, readFunc)
        self._sourceAddress: LiveIPString = LiveIPString(data["/sourceaddress"], updateFunc, readFunc)
        self._sourcePort: LiveIPInteger = LiveIPInteger(data["/sourceport"], updateFunc, readFunc)
        self._sourceAddressFilter: LiveIPBool = LiveIPBool(data["/sourceaddressfilterenabled"], updateFunc, readFunc)

    def data(self):
        result = super().data()
        result["sourceAddress"] = self._sourceAddress.getValue()
        result["sourcePort"] = self._sourcePort.getValue()
        result["sourceAddressFilter"] = self._sourceAddressFilter.getValue()
        return result

    # Getters and Setters for SourceAddress

    def get_sourceAddress_raw(self) -> LiveIPString:
        return self._sourceAddress

    def get_sourceAddress(self) -> str:
        return self._sourceAddress.getValue()

    def set_sourceAddress(self, value: str) -> None:
        self._sourceAddress.setValue(value)

    # Getters and Setters for SourcePort

    def get_sourcePort_raw(self) -> LiveIPInteger:
        return self._sourcePort

    def get_sourcePort(self) -> int:
        return self._sourcePort.getValue()

    def set_sourcePort(self, value: int) -> None:
        self._sourcePort.setValue(value)

    # Getters and Setters for SourceAddressFilter

    def get_sourceAddressFilter_raw(self) -> LiveIPBool:
        return self._sourceAddressFilter

    def get_sourceAddressFilter(self) -> bool:
        return self._sourceAddressFilter.getValue()

    def set_sourceAddressFilter(self, value: bool) -> None:
        self._sourceAddressFilter.setValue(value)


class Media:
    def __init__(self, data: dict, updateFunc: function, readFunc: function) -> None:
        # All URI should be something like /<INFO> or /redundancies/1/<INFO>
        self._stream: Stream = streamConstructor(data, updateFunc, readFunc)
        self._redundant_stream: Stream = streamConstructor(filterDown(data, "/redundancies/1"), updateFunc, readFunc)

    def data(self) -> dict:
        return {
            "stream": self._stream.data(),
            "redundant_stream": self._redundant_stream.data(),
        }

    def get_stream(self) -> Stream:
        return self._stream

    def get_redundant_stream(self) -> Stream:
        return self._redundant_stream


class Ancillary(Media):
    def __init__(self, data: dict, updateFunc, readFunc) -> None:
        super().__init__(data, updateFunc, readFunc)
        self._content: LiveIPEnum = LiveIPEnum(data["/content"], updateFunc, readFunc)
        self._redundant_content: LiveIPEnum = LiveIPEnum(data["/redundancies/1/content"], updateFunc, readFunc)

    def data(self) -> dict:
        result = super().data()
        result["content"] = self._content.getValue()
        result["redundant_content"] = self._redundant_content.getValue()
        return result

    def get_content(self) -> LiveIPEnum:
        return self._content

    def get_redundant_content(self) -> LiveIPEnum:
        return self._redundant_content


class Video(Media):
    def __init__(self, data: dict, updateFunc, readFunc) -> None:
        super().__init__(data, updateFunc, readFunc)


class Audio(Media):
    def __init__(self, data: dict, updateFunc, readFunc) -> None:
        super().__init__(data, updateFunc, readFunc)


class Channel:
    def __init__(self, data: dict, updateFunc: function, readFunc: function) -> None:
        # Going to get something like /ancillary/streams/1/sourceport
        self._anc: dict[int, Ancillary] = self.__build_type(
            filterDown(data, "/ancillary/streams"), Ancillary, updateFunc, readFunc
        )
        self._audio: dict[int, Audio] = self.__build_type(
            filterDown(data, "/audio/streams"), Audio, updateFunc, readFunc
        )

        self._video: dict[int, Video] = self.__build_type(
            filterDown(data, "/video/regular/streams"), Video, updateFunc, readFunc
        )
        self._phases: dict[int, Video] = self.__build_type(
            filterDown(data, "/video/regularslsm/streams"), Video, updateFunc, readFunc
        )

        self._audioMon: dict[int, Audio] = self.__build_type(
            filterDown(data, "/audiomonitoring/streams"), Audio, updateFunc, readFunc
        )
        self._videoMon: dict[int, Video] = self.__build_type(
            filterDown(data, "/monitoring/regular/streams"), Video, updateFunc, readFunc
        )
        # Run the Builders

    def __build_type(
        self,
        data: dict,
        NewType: classmethod,
        updateFunc: function,
        readFunc: function,
    ) -> dict[int, classmethod]:
        # From here on, URIs will be /1/<INFO>
        streamCount = findMax(data)

        result = {}

        for i in range(1, streamCount + 1):
            # This effectively gets rid of the /1 at the beginning of a stream URI
            result[i] = NewType(filterDown(data, f"/{i}"), updateFunc, readFunc)
        return result

    def data(self) -> dict:
        return {
            "ancillary": {i: anc.data() for i, anc in self._anc.items()},
            "video": {i: video.data() for i, video in self._video.items()},
            "audio": {i: audio.data() for i, audio in self._audio.items()},
            "phases": {i: phase.data() for i, phase in self._phases.items()},
            "audioMon": {i: audioMon.data() for i, audioMon in self._audioMon.items()},
            "videoMon": {i: videoMon.data() for i, videoMon in self._videoMon.items()},
        }

    def get_ancs(self) -> dict[int, Ancillary]:
        return self._anc

    def get_anc(self, i: int) -> Ancillary:
        return self._anc[i]

    def get_videos(self) -> dict[int, Video]:
        return self._video

    def get_video(self, i: int) -> Video:
        return self._video[i]

    def get_audios(self) -> dict[int, Audio]:
        return self._audio

    def get_audio(self, i: int) -> Audio:
        return self._audio[i]

    def get_phases(self) -> dict[int, Video]:
        return self._phases

    def get_phase(self, i: int) -> Video:
        return self._phases[i]

    def get_audio_mons(self) -> dict[int, Audio]:
        return self._audioMon

    def get_audio_mon(self, i: int) -> Audio:
        return self._audioMon[i]

    def get_video_mons(self) -> dict[int, Video]:
        return self._videoMon

    def get_video_mon(self, i: int) -> Video:
        return self._videoMon[i]


class InputChannel(Channel):
    def __init__(self, data: dict, updateFunc: function, readFunc: function) -> None:
        # Going to get something like /ancillary/streams/1/sourceport
        super().__init__(data, updateFunc, readFunc)


class OutputChannel(Channel):
    def __init__(self, data: dict, updateFunc: function, readFunc: function) -> None:
        # Going to get something like /ancillary/streams/1/source
        super().__init__(data, updateFunc, readFunc)


class LiveIPConfig:
    def __init__(self, data: dict, updateFunc: function, readFunc: function, numLine: int):
        self._inputs: dict[int, InputChannel] = {}
        self._outputs: dict[int, OutputChannel] = {}
        self._mv_inputs: dict[int, InputChannel] = {}
        self._mv_outputs: dict[int, OutputChannel] = {}
        self._hardware: dict[str, LiveIPBase] = {}
        self._liveIP: dict[str, LiveIPBase] = {}
        self._numLine: int = numLine
        self._updateFunc: function = updateFunc
        self._readFunc: function = readFunc

        if "Data" in data.keys():
            data = data["Data"]["Parameters"]

        for k in data.keys():
            data[k]["uri"] = k

        channels: dict = filterDown(data, "/channels")
        mvChannels: dict = filterDown(data, "/multiviewers")

        mvInChannels: dict = filterDown(mvChannels, "/ins")
        mvOutChannels: dict = filterDown(mvChannels, "/outs")

        inChannels: dict = filterDown(channels, "/ins")
        outChannels: dict = filterDown(channels, "/outs")

        self._inputs = self._build_channels(inChannels, InputChannel)
        self._outputs = self._build_channels(outChannels, OutputChannel)
        self._mv_inputs = self._build_channels(mvInChannels, InputChannel)
        self._mv_outputs = self._build_channels(mvOutChannels, OutputChannel)

        # Hardware Build
        hwData = filterDown(data, "/hardware/xhubvia")

        self._hardware["enabled"] = LiveIPBool(hwData["/enabled"], self._updateMiddleware, self._readMiddleware)
        self._hardware["qsfpPrimaryModule"] = LiveIPInteger(
            hwData["/qsfpPrimaryModule"], self._updateMiddleware, self._readMiddleware
        )
        self._hardware["qsfpSecondaryModule"] = LiveIPInteger(
            hwData["/qsfpSecondaryModule"], self._updateMiddleware, self._readMiddleware
        )

        # Builds the LiveIP Generic Info
        liveIPData = filterDown(data, "/liveip")
        for k, v in liveIPData.items():
            if v["Type"] == "Integer":
                self._liveIP[k] = LiveIPInteger(v, self._updateMiddleware, self._readMiddleware)
            elif v["Type"] == "Enumeration":
                self._liveIP[k] = LiveIPEnum(v, self._updateMiddleware, self._readMiddleware)
            elif v["Type"] == "Boolean":
                self._liveIP[k] = LiveIPBool(v, self._updateMiddleware, self._readMiddleware)

    def _updateMiddleware(self, uri: str, value: Any) -> dict:
        # This is a middleware function that is called when a channel is updated
        response = self._updateFunc(self.getNumLine(), uri, value)
        return response

    def _readMiddleware(self, uri: str) -> Any:
        response = self._readFunc(self.getNumLine(), uri)
        return response

    def _build_channels(
        self,
        data: dict,
        ChannelClass: classmethod,
    ) -> dict[int, Channel]:
        result = {}
        for i in range(1, findMax(data) + 1):
            tempData = filterDown(data, f"/{i}")
            result[i] = ChannelClass(tempData, self._updateMiddleware, self._readMiddleware)
        return result

    def getInputs(self) -> dict[int, InputChannel]:
        return self._inputs

    def getInput(self, i: int) -> InputChannel:
        return self._inputs[i]

    def getOutputs(self) -> dict[int, OutputChannel]:
        return self._outputs

    def getOutput(self, i: int) -> OutputChannel:
        return self._outputs[i]

    def getMVInputs(self) -> dict[int, InputChannel]:
        return self._mv_inputs

    def getMVInput(self, i: int) -> InputChannel:
        return self._mv_inputs[i]

    def getMVOutputs(self) -> dict[int, OutputChannel]:
        return self._mv_outputs

    def getMVOutput(self, i: int) -> OutputChannel:
        return self._mv_outputs[i]

    def getNumLine(self) -> int:
        return self._numLine

    def data(self) -> dict:
        return {
            "inputs": {i: inChannel.data() for i, inChannel in self._inputs.items()},
            "outputs": {i: outChannel.data() for i, outChannel in self._outputs.items()},
            "mv_inputs": {i: mvInChannel.data() for i, mvInChannel in self._mv_inputs.items()},
            "mv_outputs": {i: mvOutChannel.data() for i, mvOutChannel in self._mv_outputs.items()},
        }


def streamConstructor(data: dict[str, dict], updateFunc, readFunc) -> Stream:
    for k in data.keys():
        if k.endswith("/sourceaddress"):
            return InputStream(data, updateFunc, readFunc)
        else:
            return OutputStream(data, updateFunc, readFunc)


def filterDown(data: dict[str, dict], prefix: str) -> dict[str, dict]:
    """This looks at the prefix of anything and returns the items that started with that prefix then removes the prefix.

    Args:
        data (dict[str, dict]): Data from the EVS Request
        prefix (str): The Prefix you wish to query against such as /channels/ins NO ending / needed or recommended.

    Returns:
        dict[str, dict]: The new retruned dictionary with the filter applied.
    """
    result = {}
    for k, v in data.items():
        if k == prefix:
            continue
        if k.startswith(prefix):
            result[k.removeprefix(prefix)] = v
    return result


def findMax(data: dict[str, dict]) -> int:
    """This looks at the next level and so long as it is an integer it attempts to parse it out.
    For this to work the input data need to be /1/<INFO> it cannot be 1/<INFO>

    Args:
        data (dict[str, dict]): Pass in the data from EVS.

    Returns:
        int: The maximum value
    """
    maxint = -1

    for k, v in data.items():
        tempInt = int(k.split("/")[1])
        if tempInt > maxint:
            maxint = tempInt
    return maxint


def print_channels(data: dict[str, dict[int, Channel]]) -> dict:
    result = {}
    for k, v in data.items():
        result[k] = {}
        for i, j in v.items():
            result[k][i] = j.data()
            print(f"{k} | {i} | {j.data()}")
    return result


if __name__ == "__main__":
    with open("./liveIP_cfglineNum_1.json", "r") as f:
        data: dict[str, dict] = json.load(f)
    result = LiveIPConfig(data)
    jdata = print_channels(result)

    json.dump(jdata, open("debug.json", "w"), indent=4)
