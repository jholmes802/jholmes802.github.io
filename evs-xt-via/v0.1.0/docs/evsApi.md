# EVS API Documentation

## Overview
API wrapper for EVS XT-VIA servers that handles configuration and management tasks.

## Core Components

### Server Management
- Session handling
- Server configuration
- Version control
- Facility name management

### Configuration Lines
- Create/modify config lines
- Channel configuration
- Video settings
- Audio settings

### Live IP Management
- Stream configuration
- Network settings
- IP addressing
- Port management

## Usage Examples

### Server Connection

from evsApi import XtVia

server = XtVia("10.10.52.101")
server.connect()

### xtviaServer class
This class is the primary class it should be instantiated to connect to the server, you can define the level of inspection it does, it can/will collect all information about the server if you so choose. 

| Parameter | Type | Description |
| --- | --- | --- |
| *serverIP* |  string | IP address of the EVS server<br>Ex: `10.0.4.101` |
| *configsToCollect* | list | List of config types to collect.<br>Ex `[1]` or `[1,2,3,4,5]` |
| *inspection* | int | Inspection Level, the higher the int the more information is collected abou the server.<br>1 = Basic, makes simplest query to server.<br>2 = Server Status, gets the servers current status.<br>3 = Options, gets the options of the server, tells us what codes are active.<br>4 = Configs, gets the configs of the server.<br>5 = LiveIP, gets the Live IP information of the servers. |
| *sessionID* | string | Session ID of the server, if you have one already you can pass it in here otherwise it will be generated for you. |
| *singleParam* | string | Fetches a single parameter from the server, works in conjunction with the configsToCollect parameter. Allows you to get very granular information about the server. |

#### Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| *_serverIP* | string | IP address of the EVS server |
| *_facilityName* | string | Name of the server |
| *_chassis* | string | Tells us the chassis type, like XT-VIA or XT4K |
| *_version* | string | Version of Multicam |
| *_SN* | string | Serial number of the server |
| *_sessionID* | string | Current Session ID of the server |
| *_HWEdition* | string | Hardware edition of the server |
| *_serverStatus* | integer | Current status of the server, integer based on the status of multicam |
| *_latestMCInfo* | dict | Latest Multicam Information the web request. |
| *_technicalLocked* | boolean | Tells us if the server is using the technical lock password or not. |
| *_lastUpdateTS* | datetime | Last time the servers basic information was updated. |
| *_focusConfigLines* | list[int] | List of config lines to pull from the server. |
| *_configs* | dict[int, configLine] | Dictionary of config lines, keyed by the config line number. |
| *_liveIPs* | dict[int, LiveIPConfig] | Dictionary of live IP information. |
| *_options* | dict[int, bool] | Dictionary of options, keyed by the option number. |

#### Methods

| Method | Arguments | Returns | Description |
| --- | --- | --- | --- |
| *xtviaServer()* | serverIP: string,<br>configsToCollect: list[int],<br>inspection: int,<br>sessionID: string,<br>singleParam: string | None | Initializes the class and connects to the server. |
| *__str__()* | self | string | Returns a string representation of the server. |
| *_isInfoStale()* | self | boolean | Checks if the server information is stale. Based on the last update time and the time delta. |
| *_get_SessionID()* | self<br>checkStale: bool | string | Gets the session ID of the server. |
| *_get_request()* | self<br>url: string,<br>params: dict | dict | Makes a request to the server and returns the json response. |
| *_post_request()* | self<br>url: string,<br>params: dict<br>data: dict | dict | Makes a post request to the server and returns the json response. |
| *_get_multicam_info()* | self | dict | Gets the latest multicam information from the server. |
| *_get_options()* | self | None | Gets the options of the server. |
| *_get_configs()* | self<br>singleParam: string | None | Gets the configs of the server. |
| *_get_liveips()* | self | None | Gets the live IP information of the server. |
| *_get_server_status()* | self | int | Gets the server status of the server. |
| *_get_configLine_all()* | self<br>numLine:int | dict | Fetches the config Lines values from the server. |
| *_get_configLine_param()* | self<br>param: string<br>>numLine:int | dict | Fetches a single parameter from the config line. This returns more information than just the value. |
| *_update_configLine()* | self<br>numLine: int<br>cfgName: string<br>cfgValue: Any<br>save: bool = False | dict | Sends a request to the server to update a config line parameter and returns the response. |
| *_get_liveip_all()* | self | dict | Fetches the live IP information from the server and for the active config line. |
| *_get_liveip_one()* | self<br>numLine: int<br>uri: string | dict | Fetches a single Live IP URI of a specific config line. |
| *_set_liveIP_cfglineNum()* | self<br>num: int | dict | Sets the config line number and then returns the response data. |
| *_set_liveip_one()* | self<br>numLine: int<br>uri: string<br>value: string | dict | Sets a single Live IP URI of a specific config line. |
| *_commit_liveIP()* | self | dict | Commits the live IP information to the server. |
| *get_facility_name()* | self | string | Returns the facility name of the server. |
| *set_facility_name()* | self<br>name: string | None | Sets the facility name of the server. |
| *get_state()* | self | int | Returns the state of the server. |
| *get_chassis()* | self | string | Returns the chassis of the server. |
| *get_version()* | self | string | Returns the version of the server. |
| *get_SN()* | self | string | Returns the serial number of the server. |
| *get_technical_lock()* | self | boolean | Returns if the server is using the technical lock password. |
| *get_mc_info_param()* | self<br>param: string | dict | Returns a specific parameter from the multicam information. |
| *get_options()* | self | dict | Returns the options of the server. |
| *get_configs()* | self | dict[int, configLine] | Returns the configs of the server. |
| *get_config()* | self<br>i: int | configLine | Returns a specific config line of the server. |
| *get_liveips()* | self | dict[int, LiveIPConfig] | Returns the live IP information of the server. |
| *get_liveip()* | self<br>i: int | LiveIPConfig | Returns a specific live IP of the server. |
| *get_serverIP()* | self | string | Returns the server IP of the server. |
| *get_HWEdition()* | self | string | Returns the hardware edition of the server. |
| *dict()* | self | dict | Returns a dictionary representation of the server. |
