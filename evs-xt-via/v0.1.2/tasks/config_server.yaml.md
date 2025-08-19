```yaml
---
- name: Set Video Standard Field Rate
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_VIDEO_STANDARD"
    config_value: "{% raw %} {{ video_standard }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Set Video Resolution
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_VIDEO_MODE"
    config_value: "{% raw %} {{ video_resolution }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Video Codec Status
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_FIRST_CHIP_CODEC_ACTIVE_1"
    config_value: "Yes"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"


- name: Configure Video Codec
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_VIDEO_CODEC_CHOICE_1"
    config_value: "{% raw %} {{ video_codec }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Video Codec Bitrate
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_REQUESTED_VIDEO_BITRATE_1"
    config_value: "{% raw %} {{ video_bitrate }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure HDR Profile
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_HDR_PROFILE"
    config_value: "{% raw %} {{ video_hdr_profile }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Color Gamut
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_COLOR_GAMUT"
    config_value: "{% raw %} {{ video_hdr_color_gamut }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Proxy Status
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_THIRD_CHIP_CODEC_ACTIVE_1"
    config_value: "{% raw %} {{ proxy }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Proxy Codec
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_THIRD_CHIP_CODEC_CHOICE_1"
    config_value: "{% raw %} {{ proxy_codec }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"

- name: Configure Proxy Bit Rate
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    config_parameter: "CFG_PARAM_THIRD_CHIP_BITRATE"
    config_value: "{% raw %} {{ proxy_bitrate }} {% endraw %}"
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %}"
```