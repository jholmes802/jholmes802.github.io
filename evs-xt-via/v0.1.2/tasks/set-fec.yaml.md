```yaml
- name: Load Options JSON into Variable
  set_fact:
    options_json_raw: "{% raw %} {{ lookup('file', options_path) }} {% endraw %}"
  delegate_to: 127.0.0.1

- name: Remove Illegal Characters from JSON
  set_fact:
    options_json_raw: "{% raw %} {{ options_json_raw | regex_replace('(\/\/.*$)', '', multiline=True) }} {% endraw %}"
  delegate_to: 127.0.0.1

- name: Parse JSON content
  set_fact:
    options_json: "{% raw %} {{ options_json_raw }} {% endraw %}"
  delegate_to: 127.0.0.1
- debug:
    msg: "{% raw %} {{ options_json }} {% endraw %}"

- name: Modify Options JSON
  set_fact:
    options_json: "{% raw %} {{ options_json | combine(item, recursive=True) }} {% endraw %}"
  loop:
    - { "NAT_disabled": { "Enabled": true } }
    - { "qsfp_primary_module_fec": { "Enabled": true, "Value": "no_fec" } }
    - { "qsfp_secondary_module_fec": { "Enabled": true, "Value": "no_fec" } }
  delegate_to: 127.0.0.1

- name: Write Options JSON to Repo
  copy:
    content: "{% raw %} {{ options_json | to_nice_json }} {% endraw %}"
    dest: "{% raw %} {{ repo_base_path }} {% endraw %}/EVS-{% raw %} {{ serverNumber }} {% endraw %}/NMOS/options.json"
  delegate_to: 127.0.0.1
```