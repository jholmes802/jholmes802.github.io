```yaml
---
- name: Set Live IP MV Input Video Enabled
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "mv_inputs"
    channel_number: "{{ item }}"
    channel_type: "video"
    parameter: "enable"
    value: "true"
  loop: "{{ range(1, 3) | list }}"
  tags: ["enable"]

- name: Set Live IP MV Input Video Multicast
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "mv_inputs"
    channel_number: "{{ item }}"
    channel_type: "video"
    parameter: "dest_addr"
    value: "{{valid_out1_multicast}}"
  loop: "{{ range(1, 3) | list }}"
  when: route_xt_via_input

- name: Set Live IP MV Input Video Destination Port
  evs_liveip:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    channel_direction: "mv_inputs"
    channel_number: "{{ item }}"
    channel_type: "video"
    parameter: "dest_port"
    value: "{{ xt_via_2110_ip_info['RX']['MV IN '+ '{:02}'.format(item)]['UDP_PORT'] }}"
  loop: "{{ range(1, 3) | list }}"
```