# For Setting a single Live IP Value

## URL Paramters

```shell
SessionId=0122250651450851
```

## Headers

```shell
content-type: application/x-www-form-urlencoded
```


## URL

```shell
http://10.10.52.102/ipconfigurationweb/getparameterlistactionjs
```

## Body

This is the body of the request. It is Form Urlencoded.

```shell
uris: /fillandkey/outs/2/monitoring/regular/streams/1/enabled
```

## Response

```json
{
    "SessionID": "0122250651450851",
    "IsMulsetupRunning": true,
    "IsMulticamRunning": false,
    "IsBootWinsRunning": false,
    "IsTechnicalLocked": false,
    "HasSharedConfigChanged": false,
    "NeedToBeUpdated": false,
    "MonitoringNeedToBeUpdated": false,
    "IsXiP": true,
    "Data": {
        "GetParameterList": "Success",
        "Parameters": {
            "/fillandkey/outs/2/monitoring/regular/streams/1/enabled": {
                "Type": "Boolean",
                "Value": false,
                "Metadata": {
                    "Visibility": true,
                    "Editable": true,
                    "IsReboot": false,
                    "IsModified": true,
                    "IsInValid": true
                }
            }
        },
        "NotFound": []
    }
}
```

