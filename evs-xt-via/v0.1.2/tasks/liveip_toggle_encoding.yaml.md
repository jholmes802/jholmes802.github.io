```yaml
{% raw %}
- name: Set 334M Encoding Off
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_{{item}}"
    config_value: "No"
  loop: "{{ range(1, play_channels | int + 1) | list }}"

- name: Save
  ansible.builtin.import_tasks: config_save.yaml
  tags: ["save"]
  

- name: Set 334M Encoding On
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_{{item}}"
    config_value: "Yes"
  loop: "{{ range(1, play_channels | int + 1) | list }}"

- name: Save
  ansible.builtin.import_tasks: config_save.yaml
  tags: ["save"]
  

- name: Set LTC In
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_HD_LTC_TC_PGM_{{item}}"
    config_value: "In"
  loop: "{{ range(1, play_channels | int + 1) | list }}"

- name: Save
  ansible.builtin.import_tasks: config_save.yaml
  tags: ["save"]
  ```