# config_channels.yaml

```yaml
{% raw %}
---
- name: Configure Base Config
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_BASE_CONFIG"
    config_value: "{{ item.base_config }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Video Interface
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_VIDEO_3G_DUAL_MODE"
    config_value: "{{ item.video_interface }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Number of Ins
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NB_RECORDER"
    config_value: "{{ item.record_channels }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Number Of Outs
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NB_PLAYER"
    config_value: "{{ item.play_channels }}"
  loop: "{{ serverVars.config_lines }}"
  
- name: Configure Speed of SSMO 1
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_SLSM_REC_SPEED"
    config_value: "{{ item.ssmo_1_speed }}"
  loop: "{{ serverVars.config_lines }}"

- name: Config Number of SSMO 1
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_SLSM_REC_CAMERA_COUNT"
    config_value: "{{ item.ssmo_1_count }}"
  loop: "{{ serverVars.config_lines }}"


- name: Configure Speed of SSMO 2
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_SECOND_SLSM_REC_SPEED"
    config_value: "{{ item.ssmo_2_speed }}"
  loop: "{{ serverVars.config_lines }}"

- name: Config Number of SSMO 2
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_SECOND_SLSM_REC_CAMERA_COUNT"
    config_value: "{{ item.ssmo_2_count }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Number of Audio Monos
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_AUDIO_MONO_COUNT"
    config_value: "{{ item.audio_monos }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Audio MADI
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_AUDIO_MADI_INPUT_COUNT"
    config_value: "{{ item.audio_madi }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Audio Analog
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_AUDIO_ANALOG_INPUT_COUNT"
    config_value: "{{ item.audio_analog }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Audio Digital
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_AUDIO_DIGITAL_INPUT_COUNT"
    config_value: "{{ item.audio_digital }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure RS422 Port 1
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_1"
    config_value: "{{ item.rs422_1 }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure RS422 Port 2
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_2"
    config_value: "{{ item.rs422_2 }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure RS422 Port 3
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_3"
    config_value: "{{ item.rs422_3 }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure RS422 Port 4
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_4"
    config_value: "{{ item.rs422_4 }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure RS422 Port 5
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_5"
    config_value: "{{ item.rs422_5 }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure RS422 Port 6
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_6"
    config_value: "{{ item.rs422_6 }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure LSM-VIA Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_CTRL_LSM_VIA"
    config_value: "{{ item.lsm_via }}"
  loop: "{{ serverVars.config_lines }}"

- name: Configure Output Channel 1 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_PGM_1"
    config_value: "{{ item.out_channel_1.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 1

- name: Configure Output Channel 2 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_PGM_2"
    config_value: "{{ item.out_channel_2.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 2

- name: Configure Output Channel 3 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_PGM_3"
    config_value: "{{ item.out_channel_3.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 3

- name: Configure Output Channel 4 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_PGM_4"
    config_value: "{{ item.out_channel_4.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 4

- name: Configure Output Channel 5 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_PGM_5"
    config_value: "{{ item.out_channel_5.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 5

- name: Configure Output Channel 6 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_PGM_6"
    config_value: "{{ item.out_channel_6.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 6

- name: Configre Input Channel 1 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_1"
    config_value: "{{ item.in_channel_1.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 1

- name: Configure Input Channel 2 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_2"
    config_value: "{{ item.in_channel_2.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 2

- name: Configure Input Channel 3 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_3"
    config_value: "{{ item.in_channel_3.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 3

- name: Configure Input Channel 4 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_4"
    config_value: "{{ item.in_channel_4.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 4

- name: Configure Input Channel 5 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_5"
    config_value: "{{ item.in_channel_5.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 5

- name: Configure Input Channel 6 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_6"
    config_value: "{{ item.in_channel_6.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 6

- name: Configure Input Channel 7 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_7"
    config_value: "{{ item.in_channel_7.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 7

- name: Configure Input Channel 8 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_8"
    config_value: "{{ item.in_channel_8.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 8

- name: Configure Input Channel 9 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_9"
    config_value: "{{ item.in_channel_9.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 9

- name: Configure Input Channel 10 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_10"
    config_value: "{{ item.in_channel_10.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 10

- name: Configure Input Channel 11 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_11"
    config_value: "{{ item.in_channel_11.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 11

- name: Configure Input Channel 12 Name
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_NAME_REC_12"
    config_value: "{{ item.in_channel_12.name }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.record_channels >= 12

- name: Configure Output Channel 1 Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_1"
    config_value: "{{ item.out_channel_1.primary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 1

- name: Configure Output Channel 2 Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_2"
    config_value: "{{ item.out_channel_2.primary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 2

- name: Configure Output Channel 3 Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_3"
    config_value: "{{ item.out_channel_3.primary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 3
- name: Configure Output Channel 4 Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_4"
    config_value: "{{ item.out_channel_4.primary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 4

- name: Configure Output Channel 5 Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_5"
    config_value: "{{ item.out_channel_5.primary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 5

- name: Configure Output Channel 6 Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_6"
    config_value: "{{ item.out_channel_6.primary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 6

- name: Configure Output Channel 1 Secondary Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_1"
    config_value: "{{ item.out_channel_1.secondary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 1

- name: Configure Output Channel 2 Secondary Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_2"
    config_value: "{{ item.out_channel_2.secondary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 2

- name: Configure Output Channel 3 Secondary Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_3"
    config_value: "{{ item.out_channel_3.secondary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 3

- name: Configure Output Channel 4 Secondary Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_4"
    config_value: "{{ item.out_channel_4.secondary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 4

- name: Configure Output Channel 5 Secondary Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_5"
    config_value: "{{ item.out_channel_5.secondary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 5

- name: Configure Output Channel 6 Secondary Control
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_6"
    config_value: "{{ item.out_channel_6.secondary_control }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 6

- name: Configure Output Channel 1 SMPTE 334M Encoding
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_1"
    config_value: "{{ item.out_channel_1.smpte_334M_encoding }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 1 and item.video_interface == "XiP"

- name: Configure Output Channel 2 SMPTE 334M Encoding
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_2"
    config_value: "{{ item.out_channel_2.smpte_334M_encoding }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 2 and item.video_interface == "XiP"

- name: Configure Output Channel 3 SMPTE 334M Encoding
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_3"
    config_value: "{{ item.out_channel_3.smpte_334M_encoding }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 3 and item.video_interface == "XiP"

- name: Configure Output Channel 4 SMPTE 334M Encoding
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_4"
    config_value: "{{ item.out_channel_4.smpte_334M_encoding }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 4 and item.video_interface == "XiP"

- name: Configure Output Channel 5 SMPTE 334M Encoding
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_5"
    config_value: "{{ item.out_channel_5.smpte_334M_encoding }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 5 and item.video_interface == "XiP"

- name: Configure Output Channel 6 SMPTE 334M Encoding
  evs_config:
    server_ip: "{{ inventory_hostname }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ item.config_line_number }}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_6"
    config_value: "{{ item.out_channel_6.smpte_334M_encoding }}"
  loop: "{{ serverVars.config_lines }}"
  when: item.play_channels >= 6 and item.video_interface == "XiP"

```