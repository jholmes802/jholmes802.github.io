# config_name.yaml
```yaml
---
- name: Update Config Line Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_CONFIG_NAME"
    config_value: "{% raw %} {{ item.config_name }} {% endraw %} "
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "
  ```