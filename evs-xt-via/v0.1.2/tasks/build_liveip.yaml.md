```yaml
{% raw %}
---

- name: Build Multicast JSON
  evs_liveip_build:
    server_ip: "{{ ansible_host }}"
    output_path: "{{ evs_config_path }}/MulticastIP-{{ truck_num }}.json"
    multicast_sheet: "{{ inventory_dir }}/files/worksheets/NETWORK_MULTICAST_IP_A-UNIT.csv"

- name: Build LiveIP CSVs
  evs_liveip_build_csv:
    server_ip: "{{ ansible_host }}"
    liveip_data_path: "{{ evs_config_path }}/MulticastIP-{{ truck_num }}.json"
    num_in: "{{ record_channels }}"
    num_out: "{{ play_channels }}"
    slsm1: "{{ ssmo_1_count }}"
    slsm2: "{{ ssmo_2_count }}"
    slsm1spd: "{{ ssmo_1_speed }}"
    slsm2spd: "{{ ssmo_2_speed }}"
    version: "{{ multicam_version }}"
    output_path: "{{ liveip_path  }}/LiveIP_CSV_{% if ssmo_1_count | int > 0 %}{{ssmo_1_count}}-{{ssmo_1_speed}}_{% endif %}{% if ssmo_2_count | int > 0 %}_{{ssmo_2_count}}-{{ssmo_2_speed}}_{% endif %}{{ record_channels }}_IN_{{ play_channels }}__OUT.csv"

```