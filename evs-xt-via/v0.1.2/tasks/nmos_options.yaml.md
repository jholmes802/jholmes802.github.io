```yaml
---
- name: Load NMOS Options JSON into Variable
  set_fact:
    node_options_json: "{{ lookup('file', nmos_options_path) }}"
  delegate_to: 127.0.0.1

- name: Modify NMOS Options JSON
  set_fact:
    node_options_json: "{{ node_options_json | combine(item, recursive=True) }}"
  loop:
    - { "rds": {"address": "{{ hostvars['rds-145']['ansible_host'] }}:41000"} }
  delegate_to: 127.0.0.1

- name: Write NMOS Options JSON to Repo
  copy:
    content: "{{ node_options_json | to_nice_json }}"
    dest: "{{ nmos_options_path }}"
  delegate_to: 127.0.0.1

- name: Send NMOS Options JSON to Server
  shell:
    cmd: "curl --silent --user evsData:evs! ftp://{{ ansible_host }}/user/nmos_node_options.json -T {{ nmos_options_path }}"
  delegate_to: 127.0.0.1```