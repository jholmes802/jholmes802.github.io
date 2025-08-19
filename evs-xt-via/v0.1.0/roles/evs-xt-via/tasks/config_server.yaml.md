# config_server.yaml

```yaml
---
- name: Set Video Standard Field Rate
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_VIDEO_STANDARD"
    config_value: "{% raw %} {{ item.video_standard }} {% endraw %} "
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Set Video Resolution
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_VIDEO_MODE"
    config_value: "{% raw %} {{ item.video_resolution }} {% endraw %} "
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure Genlock
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_GENLOCK_INPUT"
    config_value: "{% raw %} {{ item.video_genlock }} {% endraw %} "
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "
```