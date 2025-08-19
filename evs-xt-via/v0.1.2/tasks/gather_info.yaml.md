```yaml
---
- name: Gather info about the server
  evs_facts:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
  register: evs_facts

- name: Register Server from List by Truck IP
  ansible.builtin.set_fact:
    serverVars: "{% raw %} {{ servers | selectattr('truck_ip', 'equalto', ansible_host) | first }} {% endraw %}"
  when: false

- name: Dump Server Vars
  ansible.builtin.debug:
    msg: "{% raw %} {{ serverVars }} {% endraw %}"
  when: false

- name: Load Multicast Information
  ansible.builtin.set_fact:
    xt_via_2110_ip_info: "{% raw %} {{ lookup('file', evs_config_path + '/MulticastIP-' + truck_num + '.json') }} {% endraw %}"```