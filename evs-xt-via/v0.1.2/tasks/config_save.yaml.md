```yaml
- name: Save config
  evs_config_save:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
```