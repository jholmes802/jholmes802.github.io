# config_operation.yaml
```yaml
- name: Set Clip Edit By Network
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_CLIP_EDIT_BY_NETWORK"
    config_value: "{% raw %} {{ item.clip_edit_by_network }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Set Network Copy Push
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_DEFAULT_COPY_MOVE"
    config_value: "{% raw %} {{ item.network_copy_push }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
```