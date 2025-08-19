```yaml
---
# This fetches the channel information from the server.
- name: Get Record Channel Count
  evs_config_get:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_NB_RECORDER"
  register: record_channels_get

- name: Get Number Of Outs
  evs_config_get:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_NB_PLAYER"
  register: play_channels_get

- name: Get Speed of SSMO 1
  evs_config_get:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_SLSM_REC_SPEED"
  register: ssmo_1_speed_get

- name: Get Number of SSMO 1
  evs_config_get:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_SLSM_REC_CAMERA_COUNT"
  register: ssmo_1_count_get

- name: Get Speed of SSMO 2
  evs_config_get:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_SECOND_SLSM_REC_SPEED"
  register: ssmo_2_speed_get

- name: Get Number of SSMO 2
  evs_config_get:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_SECOND_SLSM_REC_CAMERA_COUNT"
  register: ssmo_2_count_get

- name: Set the variables to the new values
  set_fact:
    record_channels: "{% raw %} {{ record_channels_get.value }} {% endraw %} "
    play_channels: "{% raw %} {{ play_channels_get.value }} {% endraw %} "
    ssmo_1_speed: "{% raw %} {{ ssmo_1_speed_get.value }} {% endraw %} "
    ssmo_1_count: "{% raw %} {{ ssmo_1_count_get.value }} {% endraw %} "
    ssmo_2_speed: "{% raw %} {{ ssmo_2_speed_get.value }} {% endraw %} "
    ssmo_2_count: "{% raw %} {{ ssmo_2_count_get.value }} {% endraw %} "
```