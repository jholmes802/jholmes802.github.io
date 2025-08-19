# config_protocol.yaml
```yaml
---
- name: Set Tally Protocol
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_TALLY_PROTOCOL"
    config_value: "{% raw %} {{ item.tally_protocol }} {% endraw %} "
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Set Tally Display Index
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_TALLY_FIRST_DISPLAY_INDEX"
    config_value: "{% raw %} {{ item.tally_display_index }} {% endraw %} "
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "
```