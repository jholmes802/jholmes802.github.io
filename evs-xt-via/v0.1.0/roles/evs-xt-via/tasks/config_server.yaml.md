# config_server.yaml

```yaml
---
- name: Set Video Standard Field Rate
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_VIDEO_STANDARD"
    config_value: "{{ item.video_standard }}"
  loop: "{{ serverVars.config_lines }}"

- name: Set Video Resolution
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_VIDEO_MODE"
    config_value: "{{ item.video_resolution }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Genlock
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_GENLOCK_INPUT"
    config_value: "{{ item.video_genlock }}"
  loop: "{{ serverVars.config_lines }}"
```