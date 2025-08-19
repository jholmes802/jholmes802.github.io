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
http://10.10.52.102/ipconfigurationweb/setparameterlistactionjs
```

## Body

This is the body of the request. It is Form Urlencoded.

```shell
/channels/outs/2/monitoring/regular/streams/1/enabled: false
/fillandkey/outs/2/monitoring/regular/streams/1/enabled: false
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
        "Status": "Success",
        "Parameters": {
            "/channels/outs/2/monitoring/regular/streams/1/enabled": {
                "SetParameterValue": "Success",
                "IsModified": true,
                "ImpactedParameters": [
                    "/fillandkey/outs/2/monitoring/regular/streams/1/enabled"
                ]
            },
            "/fillandkey/outs/2/monitoring/regular/streams/1/enabled": {
                "SetParameterValue": "Success",
                "IsModified": true
            }
        }
    }
}
```

## Notes

It is interesting that it looks like it defaults to setting the channel status and then updates the fill and key for the value you. 