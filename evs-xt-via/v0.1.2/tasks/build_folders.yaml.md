# build_folder.yaml
```yaml
---
- name: Set Base EVS Config Path
  ansible.builtin.set_fact:
    base_evs_config_path: "{% raw %} {{ inventory_dir }} {% endraw %}/files/evs-configs"

- name: Set EVS Config Path
  ansible.builtin.set_fact:
    evs_config_path: "{% raw %} {{ base_evs_config_path }} {% endraw %}/{% raw %} {{ inventory_hostname }} {% endraw %}"

- name: Set EVS Config Subfolder Path
  ansible.builtin.set_fact:
    config_line_path: "{% raw %} {{ evs_config_path }} {% endraw %}/config-lines"
    liveip_path: "{% raw %} {{ evs_config_path }} {% endraw %}/liveip"
    nmos_path: "{% raw %} {{ evs_config_path }} {% endraw %}/nmos"
    options_path: "{% raw %} {{ evs_config_path }} {% endraw %}/options"

- name: Make sure evs Folders Exist
  ansible.builtin.file:
    path: "{% raw %} {{ item }} {% endraw %}"
    state: directory
  loop:
    - "{% raw %} {{ base_evs_config_path }} {% endraw %}"
    - "{% raw %} {{ evs_config_path }} {% endraw %}"
    - "{% raw %} {{ config_line_path }} {% endraw %}"
    - "{% raw %} {{ liveip_path }} {% endraw %}"
    - "{% raw %} {{ nmos_path }} {% endraw %}"
    - "{% raw %} {{ options_path }} {% endraw %}"
```