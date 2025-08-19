```yaml
---
- name: Configure XNet Operation
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_NET_TYPE"
    config_value: "{% raw %} {{ xnet_operation }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure XNet Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_NET_HOST_NAME"
    config_value: "{% raw %} {{ xnet_name }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure XNet Number
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_NET_NUMBER"
    config_value: "{% raw %} {{ xnet_number }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure XNet Visibility
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_XNET_VISIBILITY"
    config_value: "{% raw %} {{ xnet_visibility }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure XNet Server
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_XNET_SERVER"
    config_value: "{% raw %} {{ xnet_server }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure 10Gbe Interface
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_GIGABIT_PHICAL_INTERFACE"
    config_value: "{% raw %} {{ gigabit_connection }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "
  ignore_errors: true

- name: Configure 10G Link Aggregation
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_GIGABIT_LINK_AGGREGATION"
    config_value: "{% raw %} {{ gigabit_link_agg }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "
  ignore_errors: true

- name: Configure Media Port 1 IP Address
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_EDIT_GBE1_IP_ADDRESS"
    config_value: "{% raw %} {{ media_ip }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure Media Port 1 Subnet Mask
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_EDIT_GBE1_MASK_ADDRESS"
    config_value: "{% raw %} {{ media_subnet }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure Media Port 1 Gateway
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_EDIT_GBE1_GATEWAY_ADDRESS"
    config_value: "{% raw %} {{ media_gateway }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure 2110 Port 29 IP Address
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_NETWORK_QSFP_MODULE1_PORT1_IPADDRESS"
    config_value: "{% raw %} {{ st2110_ip }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure 2110 Port 29 Subnet Mask
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_NETWORK_QSFP_MODULE1_PORT1_SUBNETMASK"
    config_value: "{% raw %} {{ st2110_subnet }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure 2110 Port 29 Gateway
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_NETWORK_QSFP_MODULE1_PORT1_DEFGATEWAY"
    config_value: "{% raw %} {{ st2110_gateway }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "
```