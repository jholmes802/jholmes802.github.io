```yaml
- name: Set Clip Edit By Network
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_CLIP_EDIT_BY_NETWORK"
    config_value: "{% raw %} {{ clip_edit_by_network }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: false

- name: Set Network Copy Push
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_DEFAULT_COPY_MOVE"
    config_value: "{% raw %} {{ network_copy_push }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
```