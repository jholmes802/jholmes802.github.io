```yaml
---
# This is going to be hardware settings and Audio settings, this might be a bit of an odd duck.
- name: Set PTP Domain
  evs_liveip_raw:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    uri: "/liveip/ptp/domain"
    value: "{{ ptp_domain }}"

- name: Set Audio Packet Timing
  evs_liveip_raw:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
    uri: "/liveip/aes67/packettime"
    value: "125"
```