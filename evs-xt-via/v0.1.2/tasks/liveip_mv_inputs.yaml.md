```yaml
---
- name: Set Live IP MV Input Video Enabled
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "mv_inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video"
    parameter: "enable"
    value: "true"
  loop: "{% raw %} {{ range(1, 3) | list }} {% endraw %} "
  tags: ["enable"]

- name: Set Live IP MV Input Video Multicast
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "mv_inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video"
    parameter: "dest_addr"
    value: "{% raw %} {{valid_out1_multicast}} {% endraw %} "
  loop: "{% raw %} {{ range(1, 3) | list }} {% endraw %} "
  when: route_xt_via_input

- name: Set Live IP MV Input Video Destination Port
  evs_liveip:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    channel_direction: "mv_inputs"
    channel_number: "{% raw %} {{ item }} {% endraw %} "
    channel_type: "video"
    parameter: "dest_port"
    value: "{% raw %} {{ xt_via_2110_ip_info['RX']['MV IN '+ '{:02}'.format(item)]['UDP_PORT'] }} {% endraw %} "
  loop: "{% raw %} {{ range(1, 3) | list }} {% endraw %} "
```