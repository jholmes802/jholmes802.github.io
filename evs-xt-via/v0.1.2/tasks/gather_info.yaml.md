```yaml
{% raw %}
---
- name: Gather info about the server
  evs_facts:
    server_ip: "{{ ansible_host }}"
  register: evs_facts

- name: Register Server from List by Truck IP
  ansible.builtin.set_fact:
    serverVars: "{{ servers | selectattr('truck_ip', 'equalto', ansible_host) | first }}"
  when: false

- name: Dump Server Vars
  ansible.builtin.debug:
    msg: "{{ serverVars }}"
  when: false

- name: Load Multicast Information
  ansible.builtin.set_fact:
    xt_via_2110_ip_info: "{{ lookup('file', evs_config_path + '/MulticastIP-' + truck_num + '.json') }}"```