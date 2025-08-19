```yaml
---
- name: Set Video Standard Field Rate
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_VIDEO_STANDARD"
    config_value: "{{ video_standard }}"
  # loop: "{{ serverVars.config_lines }}"

- name: Set Video Resolution
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_VIDEO_MODE"
    config_value: "{{ video_resolution }}"
  # loop: "{{ serverVars.config_lines }}"

- name: Configure Video Codec Status
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_FIRST_CHIP_CODEC_ACTIVE_1"
    config_value: "Yes"
  # loop: "{{ serverVars.config_lines }}"


- name: Configure Video Codec
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_VIDEO_CODEC_CHOICE_1"
    config_value: "{{ video_codec }}"
  # loop: "{{ serverVars.config_lines }}"

- name: Configure Video Codec Bitrate
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_REQUESTED_VIDEO_BITRATE_1"
    config_value: "{{ video_bitrate }}"
  # loop: "{{ serverVars.config_lines }}"

- name: Configure HDR Profile
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_HDR_PROFILE"
    config_value: "{{ video_hdr_profile }}"
  # loop: "{{ serverVars.config_lines }}"

- name: Configure Color Gamut
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_COLOR_GAMUT"
    config_value: "{{ video_hdr_color_gamut }}"
  # loop: "{{ serverVars.config_lines }}"

- name: Configure Proxy Status
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_THIRD_CHIP_CODEC_ACTIVE_1"
    config_value: "{{ proxy }}"
  # loop: "{{ serverVars.config_lines }}"

- name: Configure Proxy Codec
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_THIRD_CHIP_CODEC_CHOICE_1"
    config_value: "{{ proxy_codec }}"
  # loop: "{{ serverVars.config_lines }}"

- name: Configure Proxy Bit Rate
  evs_config:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_THIRD_CHIP_BITRATE"
    config_value: "{{ proxy_bitrate }}"
  # loop: "{{ serverVars.config_lines }}"
```