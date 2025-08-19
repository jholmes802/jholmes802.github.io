# config_channels.yaml

```yaml
---
- name: Configure Base Config
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_BASE_CONFIG"
    config_value: "{% raw %} {{ item.base_config }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Video Interface
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_VIDEO_3G_DUAL_MODE"
    config_value: "{% raw %} {{ item.video_interface }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Number of Ins
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NB_RECORDER"
    config_value: "{% raw %} {{ item.record_channels }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Number Of Outs
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NB_PLAYER"
    config_value: "{% raw %} {{ item.play_channels }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  
- name: Configure Speed of SSMO 1
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SLSM_REC_SPEED"
    config_value: "{% raw %} {{ item.ssmo_1_speed }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Config Number of SSMO 1
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SLSM_REC_CAMERA_COUNT"
    config_value: "{% raw %} {{ item.ssmo_1_count }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"


- name: Configure Speed of SSMO 2
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SECOND_SLSM_REC_SPEED"
    config_value: "{% raw %} {{ item.ssmo_2_speed }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Config Number of SSMO 2
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SECOND_SLSM_REC_CAMERA_COUNT"
    config_value: "{% raw %} {{ item.ssmo_2_count }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Number of Audio Monos
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_AUDIO_MONO_COUNT"
    config_value: "{% raw %} {{ item.audio_monos }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Audio MADI
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_AUDIO_MADI_INPUT_COUNT"
    config_value: "{% raw %} {{ item.audio_madi }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Audio Analog
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_AUDIO_ANALOG_INPUT_COUNT"
    config_value: "{% raw %} {{ item.audio_analog }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Audio Digital
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_AUDIO_DIGITAL_INPUT_COUNT"
    config_value: "{% raw %} {{ item.audio_digital }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure RS422 Port 1
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_1"
    config_value: "{% raw %} {{ item.rs422_1 }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure RS422 Port 2
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_2"
    config_value: "{% raw %} {{ item.rs422_2 }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure RS422 Port 3
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_3"
    config_value: "{% raw %} {{ item.rs422_3 }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure RS422 Port 4
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_4"
    config_value: "{% raw %} {{ item.rs422_4 }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure RS422 Port 5
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_5"
    config_value: "{% raw %} {{ item.rs422_5 }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure RS422 Port 6
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_6"
    config_value: "{% raw %} {{ item.rs422_6 }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure LSM-VIA Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_CTRL_LSM_VIA"
    config_value: "{% raw %} {{ item.lsm_via }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Output Channel 1 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_1"
    config_value: "{% raw %} {{ item.out_channel_1.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 1

- name: Configure Output Channel 2 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_2"
    config_value: "{% raw %} {{ item.out_channel_2.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 2

- name: Configure Output Channel 3 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_3"
    config_value: "{% raw %} {{ item.out_channel_3.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 3

- name: Configure Output Channel 4 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_4"
    config_value: "{% raw %} {{ item.out_channel_4.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 4

- name: Configure Output Channel 5 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_5"
    config_value: "{% raw %} {{ item.out_channel_5.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 5

- name: Configure Output Channel 6 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_6"
    config_value: "{% raw %} {{ item.out_channel_6.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 6

- name: Configre Input Channel 1 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_1"
    config_value: "{% raw %} {{ item.in_channel_1.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 1

- name: Configure Input Channel 2 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_2"
    config_value: "{% raw %} {{ item.in_channel_2.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 2

- name: Configure Input Channel 3 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_3"
    config_value: "{% raw %} {{ item.in_channel_3.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 3

- name: Configure Input Channel 4 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_4"
    config_value: "{% raw %} {{ item.in_channel_4.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 4

- name: Configure Input Channel 5 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_5"
    config_value: "{% raw %} {{ item.in_channel_5.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 5

- name: Configure Input Channel 6 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_6"
    config_value: "{% raw %} {{ item.in_channel_6.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 6

- name: Configure Input Channel 7 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_7"
    config_value: "{% raw %} {{ item.in_channel_7.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 7

- name: Configure Input Channel 8 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_8"
    config_value: "{% raw %} {{ item.in_channel_8.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 8

- name: Configure Input Channel 9 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_9"
    config_value: "{% raw %} {{ item.in_channel_9.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 9

- name: Configure Input Channel 10 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_10"
    config_value: "{% raw %} {{ item.in_channel_10.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 10

- name: Configure Input Channel 11 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_11"
    config_value: "{% raw %} {{ item.in_channel_11.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 11

- name: Configure Input Channel 12 Name
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_12"
    config_value: "{% raw %} {{ item.in_channel_12.name }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.record_channels >= 12

- name: Configure Output Channel 1 Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_1"
    config_value: "{% raw %} {{ item.out_channel_1.primary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 1

- name: Configure Output Channel 2 Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_2"
    config_value: "{% raw %} {{ item.out_channel_2.primary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 2

- name: Configure Output Channel 3 Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_3"
    config_value: "{% raw %} {{ item.out_channel_3.primary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 3
- name: Configure Output Channel 4 Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_4"
    config_value: "{% raw %} {{ item.out_channel_4.primary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 4

- name: Configure Output Channel 5 Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_5"
    config_value: "{% raw %} {{ item.out_channel_5.primary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 5

- name: Configure Output Channel 6 Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_6"
    config_value: "{% raw %} {{ item.out_channel_6.primary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 6

- name: Configure Output Channel 1 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_1"
    config_value: "{% raw %} {{ item.out_channel_1.secondary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 1

- name: Configure Output Channel 2 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_2"
    config_value: "{% raw %} {{ item.out_channel_2.secondary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 2

- name: Configure Output Channel 3 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_3"
    config_value: "{% raw %} {{ item.out_channel_3.secondary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 3

- name: Configure Output Channel 4 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_4"
    config_value: "{% raw %} {{ item.out_channel_4.secondary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 4

- name: Configure Output Channel 5 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_5"
    config_value: "{% raw %} {{ item.out_channel_5.secondary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 5

- name: Configure Output Channel 6 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_6"
    config_value: "{% raw %} {{ item.out_channel_6.secondary_control }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 6

- name: Configure Output Channel 1 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_1"
    config_value: "{% raw %} {{ item.out_channel_1.smpte_334M_encoding }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 1 and item.video_interface == "XiP"

- name: Configure Output Channel 2 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_2"
    config_value: "{% raw %} {{ item.out_channel_2.smpte_334M_encoding }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 2 and item.video_interface == "XiP"

- name: Configure Output Channel 3 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_3"
    config_value: "{% raw %} {{ item.out_channel_3.smpte_334M_encoding }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 3 and item.video_interface == "XiP"

- name: Configure Output Channel 4 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_4"
    config_value: "{% raw %} {{ item.out_channel_4.smpte_334M_encoding }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 4 and item.video_interface == "XiP"

- name: Configure Output Channel 5 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_5"
    config_value: "{% raw %} {{ item.out_channel_5.smpte_334M_encoding }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 5 and item.video_interface == "XiP"

- name: Configure Output Channel 6 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ inventory_hostname }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ item.config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_6"
    config_value: "{% raw %} {{ item.out_channel_6.smpte_334M_encoding }} {% endraw %}"
  loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: item.play_channels >= 6 and item.video_interface == "XiP"

```