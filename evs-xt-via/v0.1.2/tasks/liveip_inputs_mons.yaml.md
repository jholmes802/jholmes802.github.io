```yaml
{% raw %}
---
# Video Mon

- name: Set Live IP Input Video Mon Enabled
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "in_mon_outs"
    channel_number: "{{ item }}"
    channel_type: "video_mon"
    parameter: "enable"
    value: "true"
  loop: "{{ range(1, record_channels | int + 1) | list }}"

- name: Set Live IP Input Video Mon Multicast
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "in_mon_outs"
    channel_number: "{{ item }}"
    channel_type: "video_mon"
    parameter: "dest_addr"
    value: "{{ xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['VIDEO_PURPLE'] }}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"

- name: Set Live IP Input Video Mon Destination Port
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "in_mon_outs"
    channel_number: "{{ item }}"
    channel_type: "video_mon"
    parameter: "dest_port"
    value: "{{ xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['UDP_PORT'] }}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"

# Audio Mon G1

- name: Set Live IP Input Mon Audio G1 Enabled
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "in_mon_outs"
    channel_number: "{{ item }}"
    channel_type: "audio_mon_g1"
    parameter: "enable"
    value: "true"
  loop: "{{ range(1, record_channels | int + 1) | list }}"

- name: Set Live IP Input Mon Audio G1 Multicast
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "in_mon_outs"
    channel_number: "{{ item }}"
    channel_type: "audio_mon_g1"
    parameter: "dest_addr"
    value: "{{ xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['AUDIO_G1_PURPLE'] }}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"

- name: Set Live IP Input Mon Audio G1 Destination Port
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "in_mon_outs"
    channel_number: "{{ item }}"
    channel_type: "audio_mon_g1"
    parameter: "dest_port"
    value: "{{ xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['UDP_PORT'] }}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"

# Audio Mon G2

- name: Set Live IP Input Mon Audio G2 Enabled
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "in_mon_outs"
    channel_number: "{{ item }}"
    channel_type: "audio_mon_g2"
    parameter: "enable"
    value: "true"
  loop: "{{ range(1, record_channels | int + 1) | list }}"

- name: Set Live IP Input Mon Audio G2 Multicast
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "in_mon_outs"
    channel_number: "{{ item }}"
    channel_type: "audio_mon_g2"
    parameter: "dest_addr"
    value: "{{xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['AUDIO_G2_PURPLE'] }}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"

- name: Set Live IP Input Mon Audio G2 Destination Port
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "in_mon_outs"
    channel_number: "{{ item }}"
    channel_type: "audio_mon_g2"
    parameter: "dest_port"
    value: "{{ xt_via_2110_ip_info['TX']['MON IN '+ '{:02}'.format(item)]['UDP_PORT'] }}"
  loop: "{{ range(1, record_channels | int + 1) | list }}"
{% endraw %}
```