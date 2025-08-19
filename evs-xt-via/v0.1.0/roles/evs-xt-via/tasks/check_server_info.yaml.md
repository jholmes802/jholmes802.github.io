# check_server_info.yaml

```yaml
---

- name: Set Facility Name
  evs_server:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    facility_name: "{% raw %} {{ serverVars.facility_name }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"

```