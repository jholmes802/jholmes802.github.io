```yaml
---
# Video Output

- name: Set Live IP Output Video Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "
  # tags: ["enable"]

- name: Set Live IP Output Video Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video"
    parameter: "dest_addr"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['CLEAN OUT '+ '{:02}'.format(item) ]['VIDEO_PURPLE'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "

- name: Set Live IP Output Video Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['CLEAN OUT '+ '{:02}'.format(item) ]['UDP_PORT'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "

# Audio G1 Output

- name: Set Live IP Output Audio G1 Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_g1"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "
  tags: ["enable"]

- name: Set Live IP Output Audio G1 Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_g1"
    parameter: "dest_addr"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['CLEAN OUT '+ '{:02}'.format(item) ]['AUDIO_G1_PURPLE'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "
  

- name: Set Live IP Output Audio G1 Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_g1"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['CLEAN OUT '+ '{:02}'.format(item) ]['UDP_PORT'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "

  # Audio G2 Output

- name: Set Live IP Output Audio G2 Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_g2"
    parameter: "enable"
    value: "{% raw %} {{ evs.audio_g2 }} {% endraw %} "
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "
  tags: ["enable"]

- name: Set Live IP Output Audio G2 Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_g2"
    parameter: "dest_addr"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['CLEAN OUT '+ '{:02}'.format(item) ]['AUDIO_G2_PURPLE'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "
  

- name: Set Live IP Output Audio G2 Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "audio_g2"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['CLEAN OUT '+ '{:02}'.format(item) ]['UDP_PORT'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "

# ANC Output

- name: Set Live IP Output Anc Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "anc"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "
  # tags: ["enable"]

- name: Set Live IP Output Anc Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "anc"
    parameter: "dest_addr"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['CLEAN OUT '+ '{:02}'.format(item) ]['ANC_PURPLE'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "
  

- name: Set Live IP Output Anc Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "anc"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['CLEAN OUT '+ '{:02}'.format(item) ]['UDP_PORT'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "

# Mon Video Output

- name: Set Live IP Output Mon Video Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video_mon"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "
  tags: ["enable"]

- name: Set Live IP Output Mon Video Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video_mon"
    parameter: "dest_addr"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['MON OUT '+ '{:02}'.format(item) ]['VIDEO_PURPLE'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "
  

- name: Set Live IP Output Mon Video Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video_mon"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['MON OUT '+ '{:02}'.format(item) ]['UDP_PORT'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, play_channels | int + 1) | list }} {% endraw %} "
```