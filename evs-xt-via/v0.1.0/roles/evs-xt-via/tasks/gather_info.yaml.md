# gather_info.yaml
```yaml
---
- name: Gather info about the server
  evs_facts:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %} "
  register: evs_facts

- name: Set Truck Number Varible
  set_fact:
    truck_num: "{% raw %} {{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') }} {% endraw %} "

- name: Register Server from List by Truck IP
  set_fact:
    serverVars: "{% raw %} {{ servers | selectattr('truck_ip', 'equalto', inventory_hostname) | first }} {% endraw %} "
```