# main.yaml

```yaml
{% raw %}
servers:
  - truck_number: "{{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') | int}}"
    truck_ip: "{{ inventory_hostname }}"
    facility_name: "GCV-{{ truck_name }}-{{ truck_unit }}-EVS-{{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') }}"
    
    config_lines:
      - config_line_number: 1
        enabled: "{{ all_configLines_enabled }}"

        config_name: "8 IN 4 OUT"
        base_config: "{{ base_config }}"
              
        # Video Stuff
        video_standard: "{{ video_standard }}"
        video_resolution: "{{ video_resolution }}"
        video_bitrate: "{{ video_bitrate }}"
        video_interface: "{{ video_interface }}"
        video_codec: "{{ video_codec }}"
        video_genlock: "{{ video_genlock }}"
        # Proxy Settings
        proxy: "{{ proxy }}"
        proxy_codec: "{{ proxy_codec }}"
        proxy_bitrate: "{{ proxy_bitrate }}"
        
        # Number of Channels
        record_channels: 8
        ssmo_1_speed: "2x"
        ssmo_1_count: 0
        ssmo_2_speed: "2x"
        ssmo_2_count: 0
        play_channels: 4
        
        # Audio Stuff
        audio_madi: "{{ audio_madi }}"
        audio_analog: "{{ audio_analog }}"
        audio_digital: "{{ audio_digital }}"
        audio_monos: "{{ audio_monos }}"

        # Control Settings
        rs422_1: "{{ rs422_1 }}"
        rs422_2: "{{ rs422_2 }}"
        rs422_3: "{{ rs422_3 }}"
        rs422_4: "{{ rs422_4 }}"
        rs422_5: "{{ rs422_5 }}"
        rs422_6: "{{ rs422_6 }}"
        lsm_via: "{{ lsm_via }}"

        # Record Channels Naming and information
        in_channel_1:
          name: "{{ in_channel_1_name }}"
        in_channel_2:
          name: "{{ in_channel_2_name }}"
        in_channel_3:
          name: "{{ in_channel_3_name }}"
        in_channel_4:
          name: "{{ in_channel_4_name }}"
        in_channel_5:
          name: "{{ in_channel_5_name }}"
        in_channel_6:
          name: "{{ in_channel_6_name }}"
        in_channel_7:
          name: "{{ in_channel_7_name }}"
        in_channel_8:
          name: "{{ in_channel_8_name }}"
        in_channel_9:
          name: "{{ in_channel_9_name }}"
        in_channel_10:
          name: "{{ in_channel_10_name }}"
        in_channel_11:
          name: "{{ in_channel_11_name }}"
        in_channel_12:
          name: "{{ in_channel_12_name }}"
        

        # Output Channel Information
        out_channel_1:
          name: "{{ out_channel_1_name }}"
          primary_control: "{{ out_primary_control }}"
          secondary_control: "{{ out_secondary_control }}"
          smpte_334M_encoding: "{{ smpte_334M_encoding }}"
        out_channel_2:
          name: "{{ out_channel_2_name }}"
          primary_control: "{{ out_primary_control }}"
          secondary_control: "{{ out_secondary_control }}"
          smpte_334M_encoding: "{{ smpte_334M_encoding }}"
        out_channel_3:
          name: "{{ out_channel_3_name }}"
          primary_control: "{{ out_primary_control }}"
          secondary_control: "{{ out_secondary_control }}"
          smpte_334M_encoding: "{{ smpte_334M_encoding }}"
        out_channel_4:
          name: "{{ out_channel_4_name }}"
          primary_control: "{{ out_primary_control }}"
          secondary_control: "{{ out_secondary_control }}"
          smpte_334M_encoding: "{{ smpte_334M_encoding }}"
        out_channel_5:
          name: "{{ out_channel_5_name }}"
          primary_control: "{{ out_primary_control }}"
          secondary_control: "{{ out_secondary_control }}"
          smpte_334M_encoding: "{{ smpte_334M_encoding }}"
        out_channel_6:
          name: "{{ out_channel_6_name }}"
          primary_control: "{{ out_primary_control }}"
          secondary_control: "{{ out_secondary_control }}"
          smpte_334M_encoding: "{{ smpte_334M_encoding }}"
    

        xnet_operation: "{{ xnet_operation }}"
        xnet_name: "{{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', 'EVS \\1') }}"
        xnet_number: "{{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') | int }}"
        xnet_visibility: "{{ xnet_visibility }}"
        xnet_server: "{{ xnet_server }}"

        gigabit_connection: "{{ gigabit_connection }}"
        gigabit_link_agg: "{{ gigabit_link_agg }}"

        media_ip: "{{ inventory_hostname | regex_replace('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{0,3})$', '\\1.\\2.13.\\4') }}"
        media_gateway: "{{ inventory_hostname | regex_replace('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{0,3})$', '\\1.\\2.13.1') }}"
        media_subnet: 255.255.255.0

        mv_output_format: "{{ mv_output_format }}"

        tally_protocol: "{{ tally_protocol }}"
        tally_display_index: "{{ tally_display_index }}"

        clip_edit_by_network: "{{ clip_edit_by_network }}"

        network_copy_push: "{{ network_copy_push }}"
        ```