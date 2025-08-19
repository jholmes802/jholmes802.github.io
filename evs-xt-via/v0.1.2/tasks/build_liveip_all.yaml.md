```yaml
---
- name: Build Multicast JSON
  evs_liveip_build:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    output_path: "{% raw %} {{ evs_config_path }} {% endraw %} /MulticastIP-{% raw %} {{ truck_num }} {% endraw %} .json"
    multicast_sheet: "{% raw %} {{ inventory_dir }} {% endraw %} /files/worksheets/NETWORK_MULTICAST_IP_A-UNIT.csv"

- name: Build Many LiveIP CSVs
  evs_liveip_build_csv:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    liveip_data_path: "{% raw %} {{ evs_config_path }} {% endraw %} /MulticastIP-{% raw %} {{ truck_num }} {% endraw %} .json"
    num_in: "{% raw %} {{ item.record_channels }} {% endraw %} "
    num_out: "{% raw %} {{ item.play_channels }} {% endraw %} "
    slsm1: "{% raw %} {{ item.ssmo_1_count }} {% endraw %} "
    slsm2: "{% raw %} {{ item.ssmo_2_count }} {% endraw %} "
    slsm1spd: "{% raw %} {{ item.ssmo_1_speed }} {% endraw %} "
    slsm2spd: "{% raw %} {{ item.ssmo_2_speed }} {% endraw %} "
    version: "{% raw %} {{ multicam_version }} {% endraw %} "
    output_path: "{% raw %} {{ liveip_path  }} {% endraw %} /LiveIP_CSV_{% if item.ssmo_1_count > 0 %}{% raw %} {{item.ssmo_1_count}} {% endraw %} -{% raw %} {{item.ssmo_1_speed}} {% endraw %} _{% endif %}{% if item.ssmo_2_count > 0 %}_{% raw %} {{item.ssmo_2_count}} {% endraw %} -{% raw %} {{item.ssmo_2_speed}} {% endraw %} _{% endif %}{% raw %} {{ item.record_channels }} {% endraw %} _IN_{% raw %} {{ item.play_channels }} {% endraw %} __OUT.csv"
  loop:
    - {
        record_channels: 1,
        play_channels: 1,
        ssmo_1_count: 0,
        ssmo_1_speed: "2x",
        ssmo_2_count: 0,
        ssmo_2_speed: "2x",
      }
    - {
        record_channels: 4,
        play_channels: 4,
        ssmo_1_count: 0,
        ssmo_1_speed: "2x",
        ssmo_2_count: 0,
        ssmo_2_speed: "2x",
      }
    - {
        record_channels: 6,
        play_channels: 6,
        ssmo_1_count: 0,
        ssmo_1_speed: "2x",
        ssmo_2_count: 0,
        ssmo_2_speed: "2x",
      }
    - {
        record_channels: 8,
        play_channels: 4,
        ssmo_1_count: 0,
        ssmo_1_speed: "2x",
        ssmo_2_count: 0,
        ssmo_2_speed: "2x",
      }
    - {
        record_channels: 10,
        play_channels: 2,
        ssmo_1_count: 0,
        ssmo_1_speed: "2x",
        ssmo_2_count: 0,
        ssmo_2_speed: "2x",
      }
    - {
        record_channels: 12,
        play_channels: 0,
        ssmo_1_count: 0,
        ssmo_1_speed: "2x",
        ssmo_2_count: 0,
        ssmo_2_speed: "2x",
      }
    - {
        record_channels: 2,
        play_channels: 2,
        ssmo_1_count: 2,
        ssmo_1_speed: "8x",
        ssmo_2_count: 0,
        ssmo_2_speed: "2x",
      }
    - {
        record_channels: 3,
        play_channels: 2,
        ssmo_1_count: 2,
        ssmo_1_speed: "6x",
        ssmo_2_count: 0,
        ssmo_2_speed: "2x",
      }
    - {
        record_channels: 4,
        play_channels: 2,
        ssmo_1_count: 4,
        ssmo_1_speed: "4x",
        ssmo_2_count: 0,
        ssmo_2_speed: "2x",
      }
```