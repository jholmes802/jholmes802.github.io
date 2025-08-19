# config_protocol.yaml
```yaml
{% raw %}
---
- name: Set Tally Protocol
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_TALLY_PROTOCOL"
    config_value: "{{ item.tally_protocol }}"
  loop: "{{ serverVars.config_lines }}"

- name: Set Tally Display Index
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_TALLY_FIRST_DISPLAY_INDEX"
    config_value: "{{ item.tally_display_index }}"
  loop: "{{ serverVars.config_lines }}"
```