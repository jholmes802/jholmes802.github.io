```yaml
---
# This fetches the channel information from the server.
- name: Get Record Channel Count
  evs_config_get:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_NB_RECORDER"
  register: record_channels_get

- name: Get Number Of Outs
  evs_config_get:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_NB_PLAYER"
  register: play_channels_get

- name: Get Speed of SSMO 1
  evs_config_get:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_SLSM_REC_SPEED"
  register: ssmo_1_speed_get

- name: Get Number of SSMO 1
  evs_config_get:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_SLSM_REC_CAMERA_COUNT"
  register: ssmo_1_count_get

- name: Get Speed of SSMO 2
  evs_config_get:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_SECOND_SLSM_REC_SPEED"
  register: ssmo_2_speed_get

- name: Get Number of SSMO 2
  evs_config_get:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    config_parameter: "CFG_PARAM_SECOND_SLSM_REC_CAMERA_COUNT"
  register: ssmo_2_count_get

- name: Set the variables to the new values
  set_fact:
    record_channels: "{{ record_channels_get.value }}"
    play_channels: "{{ play_channels_get.value }}"
    ssmo_1_speed: "{{ ssmo_1_speed_get.value }}"
    ssmo_1_count: "{{ ssmo_1_count_get.value }}"
    ssmo_2_speed: "{{ ssmo_2_speed_get.value }}"
    ssmo_2_count: "{{ ssmo_2_count_get.value }}"
```