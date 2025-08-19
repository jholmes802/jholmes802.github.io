```yaml
---
- name: Set Live IP Multiviewer Output Video Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "mv_outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, 5) | list }} {% endraw %} "
  tags: ["enable"]

- name: Set Live IP Multiviewer Output Video Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "mv_outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video"
    parameter: "dest_addr"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['MV OUT '+ '{:02}'.format(item) ]['VIDEO_PURPLE'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, 5) | list }} {% endraw %} "

- name: Set Live IP Multiviewer Output Video Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "mv_outputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['TX']['MV OUT '+ '{:02}'.format(item) ]['UDP_PORT'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, 5) | list }} {% endraw %} "
```