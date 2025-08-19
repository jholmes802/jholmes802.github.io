```yaml
{% raw %}
- name: Load Options JSON into Variable
  set_fact:
    options_json_raw: "{{ lookup('file', options_path) }}"
  delegate_to: 127.0.0.1

- name: Remove Illegal Characters from JSON
  set_fact:
    options_json_raw: "{{ options_json_raw | regex_replace('(\/\/.*$)', '', multiline=True) }}"
  delegate_to: 127.0.0.1

- name: Parse JSON content
  set_fact:
    options_json: "{{ options_json_raw }}"
  delegate_to: 127.0.0.1
- debug:
    msg: "{{ options_json }}"

- name: Modify Options JSON
  set_fact:
    options_json: "{{ options_json | combine(item, recursive=True) }}"
  loop:
    - { "NAT_disabled": { "Enabled": true } }
    - { "qsfp_primary_module_fec": { "Enabled": true, "Value": "no_fec" } }
    - { "qsfp_secondary_module_fec": { "Enabled": true, "Value": "no_fec" } }
  delegate_to: 127.0.0.1

- name: Write Options JSON to Repo
  copy:
    content: "{{ options_json | to_nice_json }}"
    dest: "{{ repo_base_path }}/EVS-{{ serverNumber }}/NMOS/options.json"
  delegate_to: 127.0.0.1
{% endraw %}
```