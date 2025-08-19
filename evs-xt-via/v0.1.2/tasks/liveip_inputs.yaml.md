```yaml
---
# Main Input Stuff
- name: Set Live IP Input Video Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "video"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"
  # tags: ["enable"]
  when: ssmo_1_count == 0 and ssmo_2_count == 0

- name: Set Live IP Input Video Enabled for Phases
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item.input }} {% endraw %}"
    phase_number: "{% raw %} {{ item.phase }} {% endraw %}"
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
    {% raw %} {{ results }} {% endraw %}
  # tags: ["enable"]
  when: ssmo_1_count != 0 or ssmo_2_count != 0


- name: Set Live IP Input Video Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "video"
    parameter: "dest_addr"
    value: "{% raw %} {{valid_out1_multicast}} {% endraw %}"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"
  when: route_xt_via_input and ( ssmo_1_count == 0 and ssmo_2_count == 0 )

- name: Set Live IP Input Video Multicast for Phases
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item.input }} {% endraw %}"
    phase_number: "{% raw %} {{ item.phase }} {% endraw %}"
    channel_type: "phase"
    parameter: "dest_addr"
    value: "{% raw %} {{valid_out1_multicast}} {% endraw %}"
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
    {% raw %} {{ results }} {% endraw %}
  # tags: ["enable"]
  when: route_xt_via_input and ( ssmo_1_count != 0 or ssmo_2_count != 0 )


- name: Set Live IP Input Video Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "video"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['RX']['IN '+ '{:02}'.format(item) | string + '-01']['UDP_PORT'] }} {% endraw %}"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"
  when: ssmo_1_count == 0 and ssmo_2_count == 0

- name: Set Live IP Input Video Destination Port for Phases
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item.input }} {% endraw %}"
    phase_number: "{% raw %} {{ item.phase }} {% endraw %}"
    channel_type: "phase"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['RX']['IN '+ '{:02}'.format(item.input) | string + '-01']['UDP_PORT'] }} {% endraw %}"
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
    {% raw %} {{ results }} {% endraw %}
  # tags: ["enable"]
  when: ssmo_1_count != 0 or ssmo_2_count != 0

# Audio G1

- name: Set Live IP Input Audio G1 Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "audio_g1"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"
  # tags: ["enable"]

- name: Set Live IP Input Audio G1 Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "audio_g1"
    parameter: "dest_addr"
    value: "{% raw %} {{valid_out1_multicast_audio_g1}} {% endraw %}"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"
  when: route_xt_via_input

- name: Set Live IP Input Audio G1 Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "audio_g1"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['RX']['IN '+ '{:02}'.format(item) + '-01']['UDP_PORT'] }} {% endraw %}"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"

# Audio G2

- name: Set Live IP Input Audio G2 Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "audio_g2"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"
  tags: ["enable"]

- name: Set Live IP Input Audio G2 Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "audio_g2"
    parameter: "dest_addr"
    value: "{% raw %} {{valid_out1_multicast_audio_g2}} {% endraw %}"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"
  when: route_xt_via_input

- name: Set Live IP Input Audio G2 Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "audio_g2"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['RX']['IN '+ '{:02}'.format(item) + '-01']['UDP_PORT'] }} {% endraw %}"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"

# ANC

- name: Set Live IP Input ANC Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "anc"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"
  # tags: ["enable"]

- name: Set Live IP Input ANC Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "anc"
    parameter: "dest_addr"
    value: "{% raw %} {{valid_out1_multicast_anc}} {% endraw %}"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"
  when: route_xt_via_input

- name: Set Live IP Input ANC Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    channel_direction: "inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %}"
    channel_type: "anc"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['RX']['IN '+ '{:02}'.format(item) + '-01']['UDP_PORT'] }} {% endraw %}"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %}"
```