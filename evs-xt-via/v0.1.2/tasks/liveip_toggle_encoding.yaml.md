```yaml
- name: Set 334M Encoding Off
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_{% raw %} {{item}} {% endraw %}"
    config_value: "No"
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %}"

- name: Save
  ansible.builtin.import_tasks: config_save.yaml
  tags: ["save"]
  

- name: Set 334M Encoding On
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_{% raw %} {{item}} {% endraw %}"
    config_value: "Yes"
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %}"

- name: Save
  ansible.builtin.import_tasks: config_save.yaml
  tags: ["save"]
  

- name: Set LTC In
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_HD_LTC_TC_PGM_{% raw %} {{item}} {% endraw %}"
    config_value: "In"
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %}"

- name: Save
  ansible.builtin.import_tasks: config_save.yaml
  tags: ["save"]
  ```