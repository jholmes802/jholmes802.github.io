# build_folder.yaml
```yaml
{% raw %}
---
- name: Set Base EVS Config Path
  ansible.builtin.set_fact:
    base_evs_config_path: "{{ inventory_dir }}/files/evs-configs"

- name: Set EVS Config Path
  ansible.builtin.set_fact:
    evs_config_path: "{{ base_evs_config_path }}/{{ inventory_hostname }}"

- name: Set EVS Config Subfolder Path
  ansible.builtin.set_fact:
    config_line_path: "{{ evs_config_path }}/config-lines"
    liveip_path: "{{ evs_config_path }}/liveip"
    nmos_path: "{{ evs_config_path }}/nmos"
    options_path: "{{ evs_config_path }}/options"

- name: Make sure evs Folders Exist
  ansible.builtin.file:
    path: "{{ item }}"
    state: directory
  loop:
    - "{{ base_evs_config_path }}"
    - "{{ evs_config_path }}"
    - "{{ config_line_path }}"
    - "{{ liveip_path }}"
    - "{{ nmos_path }}"
    - "{{ options_path }}"
```