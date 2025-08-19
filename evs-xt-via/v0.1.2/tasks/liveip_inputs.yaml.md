```yaml
{% raw %}
---
# Main Input Stuff
- name: Set Live IP Input Video Enabled
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "video"
    parameter: "enable"
    value: "true"
  loop: "{{ range(1, record_channels | int + 1) | list }}"
  # tags: ["enable"]
  when: ssmo_1_count == 0 and ssmo_2_count == 0

- name: Set Live IP Input Video Enabled for Phases
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item.input }}"
    phase_number: "{{ item.phase }}"
    channel_type: "phase"
    parameter: "enable"
    value: "true"
  loop: >-
    {%- set results = [] -%}
    {%- for item in range(1, record_channels | int + 1) -%}
    {%- for phase in range(1, ssmo_1_speed.replace("x", "") | int + 1) -%}
    {%- set _ = results.append({
      "input": item,
      "phase": phase
    }) %}
    {%- endfor -%}
    {%- endfor -%}
    {{ results }}
  # tags: ["enable"]
  when: ssmo_1_count != 0 or ssmo_2_count != 0


- name: Set Live IP Input Video Multicast
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "video"
    parameter: "dest_addr"
    value: "{{valid_out1_multicast}}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"
  when: route_xt_via_input and ( ssmo_1_count == 0 and ssmo_2_count == 0 )

- name: Set Live IP Input Video Multicast for Phases
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item.input }}"
    phase_number: "{{ item.phase }}"
    channel_type: "phase"
    parameter: "dest_addr"
    value: "{{valid_out1_multicast}}"
  loop: >-
    {%- set results = [] -%}
    {%- for item in range(1, record_channels | int + 1) -%}
    {%- for phase in range(1, ssmo_1_speed.replace("x", "") | int + 1) -%}
    {%- set _ = results.append({
      "input": item,
      "phase": phase
    }) %}
    {%- endfor -%}
    {%- endfor -%}
    {{ results }}
  # tags: ["enable"]
  when: route_xt_via_input and ( ssmo_1_count != 0 or ssmo_2_count != 0 )


- name: Set Live IP Input Video Destination Port
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "video"
    parameter: "dest_port"
    value: "{{ xt_via_2110_ip_info['RX']['IN '+ '{:02}'.format(item) | string + '-01']['UDP_PORT'] }}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"
  when: ssmo_1_count == 0 and ssmo_2_count == 0

- name: Set Live IP Input Video Destination Port for Phases
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item.input }}"
    phase_number: "{{ item.phase }}"
    channel_type: "phase"
    parameter: "dest_port"
    value: "{{ xt_via_2110_ip_info['RX']['IN '+ '{:02}'.format(item.input) | string + '-01']['UDP_PORT'] }}"
  loop: >-
    {%- set results = [] -%}
    {%- for item in range(1, record_channels | int + 1) -%}
    {%- for phase in range(1, ssmo_1_speed.replace("x", "") | int + 1) -%}
    {%- set _ = results.append({
      "input": item,
      "phase": phase
    }) %}
    {%- endfor -%}
    {%- endfor -%}
    {{ results }}
  # tags: ["enable"]
  when: ssmo_1_count != 0 or ssmo_2_count != 0

# Audio G1

- name: Set Live IP Input Audio G1 Enabled
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "audio_g1"
    parameter: "enable"
    value: "true"
  loop: "{{ range(1, record_channels | int + 1) | list }}"
  # tags: ["enable"]

- name: Set Live IP Input Audio G1 Multicast
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "audio_g1"
    parameter: "dest_addr"
    value: "{{valid_out1_multicast_audio_g1}}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"
  when: route_xt_via_input

- name: Set Live IP Input Audio G1 Destination Port
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "audio_g1"
    parameter: "dest_port"
    value: "{{ xt_via_2110_ip_info['RX']['IN '+ '{:02}'.format(item) + '-01']['UDP_PORT'] }}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"

# Audio G2

- name: Set Live IP Input Audio G2 Enabled
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "audio_g2"
    parameter: "enable"
    value: "true"
  loop: "{{ range(1, record_channels | int + 1) | list }}"
  tags: ["enable"]

- name: Set Live IP Input Audio G2 Multicast
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "audio_g2"
    parameter: "dest_addr"
    value: "{{valid_out1_multicast_audio_g2}}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"
  when: route_xt_via_input

- name: Set Live IP Input Audio G2 Destination Port
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "audio_g2"
    parameter: "dest_port"
    value: "{{ xt_via_2110_ip_info['RX']['IN '+ '{:02}'.format(item) + '-01']['UDP_PORT'] }}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"

# ANC

- name: Set Live IP Input ANC Enabled
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "anc"
    parameter: "enable"
    value: "true"
  loop: "{{ range(1, record_channels | int + 1) | list }}"
  # tags: ["enable"]

- name: Set Live IP Input ANC Multicast
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "anc"
    parameter: "dest_addr"
    value: "{{valid_out1_multicast_anc}}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"
  when: route_xt_via_input

- name: Set Live IP Input ANC Destination Port
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "inputs"
    channel_number: "{{ item }}"
    channel_type: "anc"
    parameter: "dest_port"
    value: "{{ xt_via_2110_ip_info['RX']['IN '+ '{:02}'.format(item) + '-01']['UDP_PORT'] }}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"
{% endraw %}
```