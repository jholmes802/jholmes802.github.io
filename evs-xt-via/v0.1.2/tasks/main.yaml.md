```yaml
# Tasks file for EVS XT-VIA Setup and Config
- name: Poll Server
  ansible.builtin.uri:
    url: "http://{{ ansible_host }}/"
  tags: ["check-connection"]
  ignore_errors: false

- name: Set Truck Number Varible
  ansible.builtin.set_fact:
    truck_num: "{{ ansible_host | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') }}"
  tags: ["always"]

- name: Build Folders
  ansible.builtin.import_tasks: build_folders.yaml
  tags: ["always"]

- name: Build Multicast Info
  ansible.builtin.import_tasks: build_liveip.yaml
  tags: ["build_liveip"]

- name: Build Many Multicast Info
  ansible.builtin.import_tasks: build_liveip_all.yaml
  tags: ["build_liveip_all", "never"]

- name: Collect Info
  ansible.builtin.import_tasks: gather_info.yaml
  tags: ["info"]

- name: Update NMOS Node Options
  ansible.builtin.import_tasks: nmos_options.yaml
  tags: ["nmos-options"]

- name: Check Basic Info
  ansible.builtin.import_tasks: check_server_info.yaml
  tags: ["server-info"]

- name: Pull Current Configs
  ansible.builtin.import_tasks: pull_config.yaml
  tags: ["pull-config"]

- name: Update Options JSON FEC
  ansible.builtin.import_tasks: set-fec.yaml
  tags: ["fec"]
  when: no_fec

- name: Config Line Server
  ansible.builtin.import_tasks: config_server.yaml
  tags: ["config-server"]

- name: Config Channels
  ansible.builtin.import_tasks: config_channels.yaml
  tags: ["config-channels"]

- name: Config Network
  ansible.builtin.import_tasks: config_network.yaml
  tags: ["config-network"]

- name: Config Monitoring
  ansible.builtin.import_tasks: config_monitoring.yaml
  tags: ["config-monitoring"]

- name: Config Protocols
  ansible.builtin.import_tasks: config_protocol.yaml
  tags: ["config-protocol"]

- name: Config GPI
  ansible.builtin.import_tasks: config_gpi.yaml
  tags: ["config-gpi"]

- name: Config Operation
  ansible.builtin.import_tasks: config_operation.yaml
  tags: ["config-operation"]

- name: Save 1
  ansible.builtin.import_tasks: config_save.yaml
  tags: ["save"]

- name: Name Config Lines
  ansible.builtin.import_tasks: config_name.yaml
  tags: ["config-name"]

- name: Get Channel Count Info
  ansible.builtin.import_tasks: get_channel_count.yaml
  tags: ["channel-count"]

- name: Toggle 334M Encoding
  ansible.builtin.import_tasks: liveip_toggle_encoding.yaml
  tags: ["liveIP", "toggle-encoding"]

- name: LiveIP Video Config Inputs
  ansible.builtin.import_tasks: liveip_inputs.yaml
  tags: ["liveIP", "liveIP-inputs"]

- name: LiveIP Video Config Outputs
  ansible.builtin.import_tasks: liveip_outputs.yaml
  tags: ["liveIP", "liveIP-outputs"]

- name: LiveIP Video Config Inputs Mons
  ansible.builtin.import_tasks: liveip_inputs_mons.yaml
  tags: ["liveIP", "liveIP-inputs", "liveIP-mons"]

- name: LiveIP Video Config MV Inputs
  ansible.builtin.import_tasks: liveip_mv_inputs.yaml
  tags: ["liveIP", "liveIP-mv-inputs", "liveIP-mv"]

- name: LiveIP Video Config MV Outputs
  ansible.builtin.import_tasks: liveip_mv_outputs.yaml
  tags: ["liveIP", "liveIP-mv-outputs", "liveIP-mv"]

- name: LiveIP Options
  ansible.builtin.import_tasks: liveip_options.yaml
  tags: ["liveIP", "liveIP-options"]

- name: Save
  ansible.builtin.import_tasks: config_save.yaml
  tags: ["save"]
```