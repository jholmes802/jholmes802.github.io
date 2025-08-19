# config_network.yaml
```yaml
{% raw %}
---
- name: Configure XNet Operation
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NET_TYPE"
    config_value: "{{ item.xnet_operation }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure XNet Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NET_HOST_NAME"
    config_value: "{{ item.xnet_name }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure XNet Number
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NET_NUMBER"
    config_value: "{{ item.xnet_number }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure XNet Visibility
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_XNET_VISIBILITY"
    config_value: "{{ item.xnet_visibility }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure XNet Server
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_XNET_SERVER"
    config_value: "{{ item.xnet_server }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure 10Gbe Interface 
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_GIGABIT_PHICAL_INTERFACE"
    config_value: "{{ item.gigabit_connection }}"
  loop: "{{ serverVars.config_lines }}"
  
- name: Configure 10G Link Aggregation
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_GIGABIT_LINK_AGGREGATION"
    config_value: "{{ item.gigabit_link_agg }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Media Port 1 IP Address
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_EDIT_GBE1_IP_ADDRESS"
    config_value: "{{ item.media_ip }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Media Port 1 Subnet Mask
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_EDIT_GBE1_MASK_ADDRESS"
    config_value: "{{ item.media_subnet }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Media Port 1 Gateway
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_EDIT_GBE1_GATEWAY_ADDRESS"
    config_value: "{{ item.media_gateway }}"
  loop: "{{ serverVars.config_lines }}"
{% endraw %}
```