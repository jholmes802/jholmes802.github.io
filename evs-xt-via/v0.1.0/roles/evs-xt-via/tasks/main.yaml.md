# main.yaml
```yaml
# Tasks file for EVS XT-VIA Setup and Config

- name: Collect Info
  import_tasks: gather_info.yaml

- name: Check Basic Info
  import_tasks: check_server_info.yaml

- name: Name Config Lines
  import_tasks: config_name.yaml

- name: Config Line Server
  import_tasks: config_server.yaml

- name: Config Channels
  import_tasks: config_channels.yaml

- name: Config Network
  import_tasks: config_network.yaml

- name: Config Monitoring
  import_tasks: config_monitoring.yaml

- name: Config Protocols
  import_tasks: config_protocol.yaml

- name: Config GPI
  import_tasks: config_gpi.yaml

- name: Config Operation
  import_tasks: config_operation.yaml
```