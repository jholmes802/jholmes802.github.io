```yaml
---
- name: Load NMOS Options JSON into Variable
  set_fact:
    node_options_json: "{% raw %} {{ lookup('file', nmos_options_path) }} {% endraw %} "
  delegate_to: 127.0.0.1

- name: Modify NMOS Options JSON
  set_fact:
    node_options_json: "{% raw %} {{ node_options_json | combine(item, recursive=True) }} {% endraw %} "
  loop:
    - { "rds": {"address": "{% raw %} {{ hostvars['rds-145']['ansible_host'] }} {% endraw %} :41000"} }
  delegate_to: 127.0.0.1

- name: Write NMOS Options JSON to Repo
  copy:
    content: "{% raw %} {{ node_options_json | to_nice_json }} {% endraw %} "
    dest: "{% raw %} {{ nmos_options_path }} {% endraw %} "
  delegate_to: 127.0.0.1

- name: Send NMOS Options JSON to Server
  shell:
    cmd: "curl --silent --user evsData:evs! ftp://{% raw %} {{ ansible_host }} {% endraw %} /user/nmos_node_options.json -T {% raw %} {{ nmos_options_path }} {% endraw %} "
  delegate_to: 127.0.0.1```