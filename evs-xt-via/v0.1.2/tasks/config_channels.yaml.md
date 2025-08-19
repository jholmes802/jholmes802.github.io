```yaml
---
- name: Configure Base Config
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_BASE_CONFIG"
    config_value: "{% raw %} {{ base_config }} {% endraw %}"


- name: Configure Video Interface
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_VIDEO_3G_DUAL_MODE"
    config_value: "{% raw %} {{ video_interface }} {% endraw %}"
  # # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Genlock
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_GENLOCK_INPUT"
    config_value: "{% raw %} {{ video_genlock }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Number of Ins
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NB_RECORDER"
    config_value: "{% raw %} {{ record_channels }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Ins Disk Use
  evs_config_disk_use:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channels_in: "{% raw %} {{ record_channels }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Number Of Outs
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NB_PLAYER"
    config_value: "{% raw %} {{ play_channels }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Speed of SSMO 1
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SLSM_REC_SPEED"
    config_value: "{% raw %} {{ ssmo_1_speed }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Config Number of SSMO 1
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SLSM_REC_CAMERA_COUNT"
    config_value: "{% raw %} {{ ssmo_1_count }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Speed of SSMO 2
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SECOND_SLSM_REC_SPEED"
    config_value: "{% raw %} {{ ssmo_2_speed }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Config Number of SSMO 2
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SECOND_SLSM_REC_CAMERA_COUNT"
    config_value: "{% raw %} {{ ssmo_2_count }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Number of Audio Monos
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_AUDIO_MONO_COUNT"
    config_value: "{% raw %} {{ audio_monos }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Audio MADI
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_AUDIO_MADI_INPUT_COUNT"
    config_value: "{% raw %} {{ audio_madi }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Audio Analog
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_AUDIO_ANALOG_INPUT_COUNT"
    config_value: "{% raw %} {{ audio_analog }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Audio Digital
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_AUDIO_DIGITAL_INPUT_COUNT"
    config_value: "{% raw %} {{ audio_digital }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Audio Ins
  evs_config_audio:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    audio_type: "{% raw %} {{ in_audio_type }} {% endraw %}"
    audio_direction: "In"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Audio Out
  evs_config_audio:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    audio_type: "{% raw %} {{ out_audio_type }} {% endraw %}"
    audio_direction: "Out"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"


- name: Configure RS422 Port 1
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_1"
    config_value: "{% raw %} {{ rs422_1 }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure RS422 Port 2
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_2"
    config_value: "{% raw %} {{ rs422_2 }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure RS422 Port 3
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_3"
    config_value: "{% raw %} {{ rs422_3 }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure RS422 Port 4
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_4"
    config_value: "{% raw %} {{ rs422_4 }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure RS422 Port 5
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_5"
    config_value: "{% raw %} {{ rs422_5 }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure RS422 Port 6
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_RS422_RESOURCE_6"
    config_value: "{% raw %} {{ rs422_6 }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure LSM-VIA Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_CTRL_LSM_VIA"
    config_value: "{% raw %} {{ lsm_via }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Output Channel 1 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_1"
    config_value: "{% raw %} {{ out_channel_1.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 1

- name: Configure Output Channel 2 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_2"
    config_value: "{% raw %} {{ out_channel_2.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 2

- name: Configure Output Channel 3 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_3"
    config_value: "{% raw %} {{ out_channel_3.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 3

- name: Configure Output Channel 4 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_4"
    config_value: "{% raw %} {{ out_channel_4.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 4

- name: Configure Output Channel 5 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_5"
    config_value: "{% raw %} {{ out_channel_5.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 5

- name: Configure Output Channel 6 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_PGM_6"
    config_value: "{% raw %} {{ out_channel_6.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 6

- name: Configre Input Channel 1 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_1"
    config_value: "{% raw %} {{ in_channel_1.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 1

- name: Configre Input Channel 1 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_1"
    config_value: "{% raw %} {{ in_channel_1.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 1 and in_channel_1.primary_control is defined

- name: Configre Input Channel 1 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_1"
    config_value: "{% raw %} {{ in_channel_1.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 1 and in_channel_1.primary_port is defined

- name: Configure Input Channel 2 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_2"
    config_value: "{% raw %} {{ in_channel_2.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 2

- name: Configre Input Channel 2 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_2"
    config_value: "{% raw %} {{ in_channel_2.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 2 and in_channel_2.primary_control is defined

- name: Configre Input Channel 2 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_2"
    config_value: "{% raw %} {{ in_channel_2.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 2 and in_channel_2.primary_port is defined

- name: Configure Input Channel 3 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_3"
    config_value: "{% raw %} {{ in_channel_3.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 3

- name: Configre Input Channel 3 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_3"
    config_value: "{% raw %} {{ in_channel_3.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 3 and in_channel_3.primary_control is defined

- name: Configre Input Channel 3 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_3"
    config_value: "{% raw %} {{ in_channel_3.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 3 and in_channel_3.primary_port is defined

- name: Configure Input Channel 4 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_4"
    config_value: "{% raw %} {{ in_channel_4.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 4

- name: Configre Input Channel 4 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_4"
    config_value: "{% raw %} {{ in_channel_4.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 4 and in_channel_4.primary_control is defined

- name: Configre Input Channel 4 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_4"
    config_value: "{% raw %} {{ in_channel_4.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 4 and in_channel_4.primary_port is defined

- name: Configure Input Channel 5 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_5"
    config_value: "{% raw %} {{ in_channel_5.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 5

- name: Configre Input Channel 5 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_5"
    config_value: "{% raw %} {{ in_channel_5.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 5 and in_channel_5.primary_control is defined

- name: Configre Input Channel 5 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_5"
    config_value: "{% raw %} {{ in_channel_5.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 5 and in_channel_5.primary_port is defined

- name: Configure Input Channel 6 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_6"
    config_value: "{% raw %} {{ in_channel_6.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 6

- name: Configre Input Channel 6 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_6"
    config_value: "{% raw %} {{ in_channel_6.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 6 and in_channel_6.primary_control is defined

- name: Configre Input Channel 6 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_6"
    config_value: "{% raw %} {{ in_channel_6.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 6 and in_channel_6.primary_port is defined

- name: Configure Input Channel 7 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_7"
    config_value: "{% raw %} {{ in_channel_7.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 7

- name: Configre Input Channel 7 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_7"
    config_value: "{% raw %} {{ in_channel_7.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 7 and in_channel_7.primary_control is defined

- name: Configre Input Channel 7 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_7"
    config_value: "{% raw %} {{ in_channel_7.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 7 and in_channel_7.primary_port is defined

- name: Configure Input Channel 8 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_8"
    config_value: "{% raw %} {{ in_channel_8.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 8

- name: Configre Input Channel 8 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_8"
    config_value: "{% raw %} {{ in_channel_8.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 8 and in_channel_8.primary_control is defined

- name: Configre Input Channel 8 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_8"
    config_value: "{% raw %} {{ in_channel_8.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 8 and in_channel_8.primary_port is defined

- name: Configure Input Channel 9 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_9"
    config_value: "{% raw %} {{ in_channel_9.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 9

- name: Configre Input Channel 9 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_9"
    config_value: "{% raw %} {{ in_channel_9.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 9 and in_channel_9.primary_control is defined

- name: Configre Input Channel 9 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_9"
    config_value: "{% raw %} {{ in_channel_1.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 9 and in_channel_9.primary_port is defined

- name: Configure Input Channel 10 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_10"
    config_value: "{% raw %} {{ in_channel_10.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 10

- name: Configre Input Channel 10 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_10"
    config_value: "{% raw %} {{ in_channel_10.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 10 and in_channel_10.primary_control is defined

- name: Configre Input Channel 10 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_10"
    config_value: "{% raw %} {{ in_channel_10.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 10 and in_channel_10.primary_port is defined

- name: Configure Input Channel 11 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_11"
    config_value: "{% raw %} {{ in_channel_11.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 11

- name: Configre Input Channel 11 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_11"
    config_value: "{% raw %} {{ in_channel_11.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 11 and in_channel_11.primary_control is defined

- name: Configre Input Channel 11 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_11"
    config_value: "{% raw %} {{ in_channel_11.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 11 and in_channel_11.primary_port is defined

- name: Configure Input Channel 12 Name
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_NAME_REC_12"
    config_value: "{% raw %} {{ in_channel_12.name }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 12

- name: Configre Input Channel 12 Primary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_CTRL_12"
    config_value: "{% raw %} {{ in_channel_12.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 12 and in_channel_12.primary_control is defined

- name: Configre Input Channel 12 Primary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REC_PORT_12"
    config_value: "{% raw %} {{ in_channel_12.primary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: record_channels | int >= 12 and in_channel_12.primary_port is defined

- name: Configure Output Channel 1 Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_1"
    config_value: "{% raw %} {{ out_channel_1.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 1

- name: Configure Output Channel 2 Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_2"
    config_value: "{% raw %} {{ out_channel_2.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 2

- name: Configure Output Channel 3 Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_3"
    config_value: "{% raw %} {{ out_channel_3.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 3
- name: Configure Output Channel 4 Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_4"
    config_value: "{% raw %} {{ out_channel_4.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 4

- name: Configure Output Channel 5 Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_5"
    config_value: "{% raw %} {{ out_channel_5.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 5

- name: Configure Output Channel 6 Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_CTRL_6"
    config_value: "{% raw %} {{ out_channel_6.primary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 6

- name: Configure Output Channel 1 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_1"
    config_value: "{% raw %} {{ out_channel_1.secondary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 1

- name: Configure Output Channel 1 Secondary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_PORT_1"
    config_value: "{% raw %} {{ out_channel_1.secondary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 1 and out_channel_1.secondary_control == "EVS IPDP" and false

- name: Configure Output Channel 2 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_2"
    config_value: "{% raw %} {{ out_channel_2.secondary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 2

- name: Configure Output Channel 2 Secondary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_PORT_2"
    config_value: "{% raw %} {{ out_channel_2.secondary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 2 and out_channel_2.secondary_control == "EVS IPDP" and false

- name: Configure Output Channel 3 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_3"
    config_value: "{% raw %} {{ out_channel_3.secondary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 3

- name: Configure Output Channel 3 Secondary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_PORT_3"
    config_value: "{% raw %} {{ out_channel_3.secondary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 3 and out_channel_3.secondary_control == "EVS IPDP"

- name: Configure Output Channel 4 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_4"
    config_value: "{% raw %} {{ out_channel_4.secondary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 4

- name: Configure Output Channel 4 Secondary Port
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_PORT_4"
    config_value: "{% raw %} {{ out_channel_4.secondary_port }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 4 and out_channel_4.secondary_control == "EVS IPDP"

- name: Configure Output Channel 5 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_5"
    config_value: "{% raw %} {{ out_channel_5.secondary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 5

- name: Configure Output Channel 6 Secondary Control
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_PLAY_SECONDARY_CTRL_6"
    config_value: "{% raw %} {{ out_channel_6.secondary_control }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 6

- name: Configure Output Channel 1 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_1"
    config_value: "{% raw %} {{ out_channel_1.smpte_334M_encoding }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 1 and video_interface == "XiP"

- name: Configure Output Channel 2 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_2"
    config_value: "{% raw %} {{ out_channel_2.smpte_334M_encoding }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 2 and video_interface == "XiP"

- name: Configure Output Channel 3 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_3"
    config_value: "{% raw %} {{ out_channel_3.smpte_334M_encoding }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 3 and video_interface == "XiP"

- name: Configure Output Channel 4 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_4"
    config_value: "{% raw %} {{ out_channel_4.smpte_334M_encoding }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 4 and video_interface == "XiP"

- name: Configure Output Channel 5 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_5"
    config_value: "{% raw %} {{ out_channel_5.smpte_334M_encoding }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 5 and video_interface == "XiP"

- name: Configure Output Channel 6 SMPTE 334M Encoding
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_SMPTE334_ENCODING_PGM_6"
    config_value: "{% raw %} {{ out_channel_6.smpte_334M_encoding }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 6 and video_interface == "XiP"

- name: Configure Output Channel 1 Mix On One Channel
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_MIX_ON_ONE_CHANNEL_1"
    config_value: "{% raw %} {{ out_channel_1.mix_one_channel }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 1

- name: Configure Output Channel 2 Mix On One Channel
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_MIX_ON_ONE_CHANNEL_2"
    config_value: "{% raw %} {{ out_channel_2.mix_one_channel }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 2

- name: Configure Output Channel 3 Mix On One Channel
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_MIX_ON_ONE_CHANNEL_3"
    config_value: "{% raw %} {{ out_channel_3.mix_one_channel }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 3

- name: Configure Output Channel 4 Mix On One Channel
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_MIX_ON_ONE_CHANNEL_4"
    config_value: "{% raw %} {{ out_channel_4.mix_one_channel }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 4

- name: Configure Output Channel 5 Mix On One Channel
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_MIX_ON_ONE_CHANNEL_5"
    config_value: "{% raw %} {{ out_channel_5.mix_one_channel }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 5

- name: Configure Output Channel 6 Mix On One Channel
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_MIX_ON_ONE_CHANNEL_6"
    config_value: "{% raw %} {{ out_channel_6.mix_one_channel }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
  when: play_channels | int >= 6
```