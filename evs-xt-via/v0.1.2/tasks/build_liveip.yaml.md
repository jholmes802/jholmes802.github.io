```yaml
---

- name: Build Multicast JSON
  evs_liveip_build:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    output_path: "{% raw %} {{ evs_config_path }} {% endraw %} /MulticastIP-{% raw %} {{ truck_num }} {% endraw %} .json"
    multicast_sheet: "{% raw %} {{ inventory_dir }} {% endraw %} /files/worksheets/NETWORK_MULTICAST_IP_A-UNIT.csv"

- name: Build LiveIP CSVs
  evs_liveip_build_csv:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    liveip_data_path: "{% raw %} {{ evs_config_path }} {% endraw %} /MulticastIP-{% raw %} {{ truck_num }} {% endraw %} .json"
    num_in: "{% raw %} {{ record_channels }} {% endraw %} "
    num_out: "{% raw %} {{ play_channels }} {% endraw %} "
    slsm1: "{% raw %} {{ ssmo_1_count }} {% endraw %} "
    slsm2: "{% raw %} {{ ssmo_2_count }} {% endraw %} "
    slsm1spd: "{% raw %} {{ ssmo_1_speed }} {% endraw %} "
    slsm2spd: "{% raw %} {{ ssmo_2_speed }} {% endraw %} "
    version: "{% raw %} {{ multicam_version }} {% endraw %} "
    output_path: "{% raw %} {{ liveip_path  }} {% endraw %} /LiveIP_CSV_{% if ssmo_1_count | int > 0 %}{% raw %} {{ssmo_1_count}} {% endraw %} -{% raw %} {{ssmo_1_speed}} {% endraw %} _{% endif %}{% if ssmo_2_count | int > 0 %}_{% raw %} {{ssmo_2_count}} {% endraw %} -{% raw %} {{ssmo_2_speed}} {% endraw %} _{% endif %}{% raw %} {{ record_channels }} {% endraw %} _IN_{% raw %} {{ play_channels }} {% endraw %} __OUT.csv"

```