```yaml
{% raw %}
---
- name: Set Live IP Multiviewer Output Video Enabled
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "mv_outputs"
    channel_number: "{{ item }}"
    channel_type: "video"
    parameter: "enable"
    value: "true"
  loop: "{{ range(1, 5) | list }}"
  tags: ["enable"]

- name: Set Live IP Multiviewer Output Video Multicast
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "mv_outputs"
    channel_number: "{{ item }}"
    channel_type: "video"
    parameter: "dest_addr"
    value: "{{ xt_via_2110_ip_info['TX']['MV OUT '+ '{:02}'.format(item) ]['VIDEO_PURPLE'] }}"
  loop: "{{ range(1, 5) | list }}"

- name: Set Live IP Multiviewer Output Video Destination Port
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "mv_outputs"
    channel_number: "{{ item }}"
    channel_type: "video"
    parameter: "dest_port"
    value: "{{ xt_via_2110_ip_info['TX']['MV OUT '+ '{:02}'.format(item) ]['UDP_PORT'] }}"
  loop: "{{ range(1, 5) | list }}"
```