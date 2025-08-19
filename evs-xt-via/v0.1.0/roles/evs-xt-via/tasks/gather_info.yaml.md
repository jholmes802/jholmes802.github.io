# gather_info.yaml
```yaml
---
- name: Gather info about the server
  evs_facts:
    server_ip: "{{ inventory_hostname }}"
  register: evs_facts

- name: Set Truck Number Varible
  set_fact:
    truck_num: "{{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') }}"

- name: Register Server from List by Truck IP
  set_fact:
    serverVars: "{{ servers | selectattr('truck_ip', 'equalto', inventory_hostname) | first }}"
```