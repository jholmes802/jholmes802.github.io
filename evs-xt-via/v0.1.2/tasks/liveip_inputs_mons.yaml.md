```yaml
---
# Video Mon

- name: Set Live IP Input Video Mon Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "in_mon_outs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video_mon"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %} "

- name: Set Live IP Input Video Mon Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "in_mon_outs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video_mon"
    parameter: "dest_addr"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['VIDEO_PURPLE'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %} "

- name: Set Live IP Input Video Mon Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "in_mon_outs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video_mon"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['UDP_PORT'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %} "

# Audio Mon G1

- name: Set Live IP Input Mon Audio G1 Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "in_mon_outs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_mon_g1"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %} "

- name: Set Live IP Input Mon Audio G1 Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "in_mon_outs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_mon_g1"
    parameter: "dest_addr"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['AUDIO_G1_PURPLE'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %} "

- name: Set Live IP Input Mon Audio G1 Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "in_mon_outs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_mon_g1"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['UDP_PORT'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %} "

# Audio Mon G2

- name: Set Live IP Input Mon Audio G2 Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "in_mon_outs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_mon_g2"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %} "

- name: Set Live IP Input Mon Audio G2 Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "in_mon_outs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_mon_g2"
    parameter: "dest_addr"
    value: "{% raw %} {{xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['AUDIO_G2_PURPLE'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %} "

- name: Set Live IP Input Mon Audio G2 Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "in_mon_outs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_mon_g2"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['UDP_PORT'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, record_channels | int + 1) | list }} {% endraw %} "
```