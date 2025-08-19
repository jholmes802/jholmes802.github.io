# config_monitoring.yaml
```yaml
{% raw %}
---
- name: Configure Base Config
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_QS_HD_OUTPUT_FORMAT"
    config_value: "{{ item.mv_output_format }}"
  loop: "{{ serverVars.config_lines }}"

```