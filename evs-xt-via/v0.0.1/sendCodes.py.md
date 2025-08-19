# sendCodes.py
```python
#!/bin/python3
import requests
import json, re, os


def getSN(serverIP: str):
    url = f"http://{serverIP}/cfgweb/CfgWeb.dll/MulticamInfoJS?SessionId=Reset"
    headers = {"Content-Type": "application/json"}

    r = requests.post(url, headers=headers)
    if r.json():
        return r.json()["SN"]
    else:
        print("No SN found")
        return None


def findFiles(path: str, sn: str):
    files = os.listdir(path)
    result = []
    for file in files:
        print(file)
        if re.search(sn, file) is not None:
            result.append(path + file)
    return result


def sendCodes(path, serverIP: str):
    url = f"http://{serverIP}/cfgweb/CfgWeb.dll/SendOptionCodesHTML?SessionID=Reset"
    with open(path, "rb") as f:
        r = requests.post(url, files={"FileCode": f})
    print(r.text)
    return r.text


def main(serverIP: str):
    sn = getSN(serverIP)
    files = findFiles("./codes/XT-VIA/110-41/110/", sn)
    for f in files:
        print(f)
        sendCodes(f, serverIP)


if __name__ == "__main__":
    server = []
    for s in server:
        main(s)
```