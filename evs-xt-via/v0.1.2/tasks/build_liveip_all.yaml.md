```yaml
{% raw %}
---
- name: Build Multicast JSON
  evs_liveip_build:
    server_ip: "{{ ansible_host }}"
    output_path: "{{ evs_config_path }}/MulticastIP-{{ truck_num }}.json"
    multicast_sheet: "{{ inventory_dir }}/files/worksheets/NETWORK_MULTICAST_IP_A-UNIT.csv"

- name: Build Many LiveIP CSVs
  evs_liveip_build_csv:
    server_ip: "{{ ansible_host }}"
    liveip_data_path: "{{ evs_config_path }}/MulticastIP-{{ truck_num }}.json"
    num_in: "{{ item.record_channels }}"
    num_out: "{{ item.play_channels }}"
    slsm1: "{{ item.ssmo_1_count }}"
    slsm2: "{{ item.ssmo_2_count }}"
    slsm1spd: "{{ item.ssmo_1_speed }}"
    slsm2spd: "{{ item.ssmo_2_speed }}"
    version: "{{ multicam_version }}"
    output_path: "{{ liveip_path  }}/LiveIP_CSV_{% if item.ssmo_1_count > 0 %}{{item.ssmo_1_count}}-{{item.ssmo_1_speed}}_{% endif %}{% if item.ssmo_2_count > 0 %}_{{item.ssmo_2_count}}-{{item.ssmo_2_speed}}_{% endif %}{{ item.record_channels }}_IN_{{ item.play_channels }}__OUT.csv"
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
{% endraw %}
```