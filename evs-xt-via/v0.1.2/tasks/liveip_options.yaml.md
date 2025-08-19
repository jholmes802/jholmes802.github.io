```yaml
---
# This is going to be hardware settings and Audio settings, this might be a bit of an odd duck.
- name: Set PTP Domain
  evs_liveip_raw:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    uri: "/liveip/ptp/domain"
    value: "{% raw %} {{ ptp_domain }} {% endraw %}"

- name: Set Audio Packet Timing
  evs_liveip_raw:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %}"
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %}"
    line_number: "{% raw %} {{ config_line_number }} {% endraw %}"
    uri: "/liveip/aes67/packettime"
    value: "125"
```