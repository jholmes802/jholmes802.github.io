```yaml
---
- name: Set Facility Name
  evs_server:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    facility_name: "{% raw %} {{ facility_name }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
```