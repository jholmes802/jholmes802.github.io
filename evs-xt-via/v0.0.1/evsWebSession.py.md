# evsWebSession.py

```python
import requests
import json
from EVSConfig import cfgLine


class session:
    def __init__(self, serverPCLanIP):
        self._serverIP = serverPCLanIP
        self._serverBaseURL = "http://" + self._serverIP

    def initConnection(self):
        req = requests.post(self._serverBaseURL + "/cfgweb/CfgWeb.dll/ConfigLinesJS?SessionID=Reset")
        text = req.text
        jsonObj = json.loads(text)
        self._sessionID: str = jsonObj["SessionID"]
        self._isMulsetupRunning: bool = jsonObj["IsMulsetupRunning"]
        self._isMulticamRunning: bool = jsonObj["IsMulticamRunning"]
        self._isTechnicalLockecd: bool = jsonObj["IsTechnicalLocked"]
        self._cfgLines: list[cfgLine] = [cfgLine(x) for x in jsonObj["Lines"]]

    def getConfigLine(self, lineNumber: int):
        for line in self._cfgLines:
            if line._number == lineNumber:
                reqUrl = f"{self._serverBaseURL}cfgweb/CfgWeb.dll/GetConfigValuesJS?SessionID=Reset&NumLine={lineNumber}&Meta=true&Reset=false&All=true"
                req = requests.post(reqUrl)
                text = req.text
                jsonObj = json.loads(text)
                line.loadComplete(jsonObj)
                return line
        return None


if __name__ == "__main__":
    xt = session("IPADDRESSHERE")
    xt.initConnection()
```