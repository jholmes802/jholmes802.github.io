```yaml
{% raw %}
- name: Set Clip Edit By Network
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_CLIP_EDIT_BY_NETWORK"
    config_value: "{{ clip_edit_by_network }}"
  # loop: "{{ serverVars.config_lines }}"
  when: false

- name: Set Network Copy Push
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_DEFAULT_COPY_MOVE"
    config_value: "{{ network_copy_push }}"
  # loop: "{{ serverVars.config_lines }}"
```