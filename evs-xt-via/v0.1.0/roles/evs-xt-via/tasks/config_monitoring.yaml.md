# config_monitoring.yaml
```yaml
---
- name: Configure Base Config
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_QS_HD_OUTPUT_FORMAT"
    config_value: "{% raw %} {{ item.mv_output_format }} {% endraw %} "
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

```