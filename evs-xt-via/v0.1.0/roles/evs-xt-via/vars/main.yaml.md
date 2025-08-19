# main.yaml

```yaml
servers:
  - truck_number: "{% raw %} {{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') | int}} {% endraw %} "
    truck_ip: "{% raw %} {{ inventory_hostname }} {% endraw %} "
    facility_name: "GCV-{% raw %} {{ truck_name }} {% endraw %} -{% raw %} {{ truck_unit }} {% endraw %} -EVS-{% raw %} {{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') }} {% endraw %} "
    
    config_lines:
      - config_line_number: 1
        enabled: "{% raw %} {{ all_configLines_enabled }} {% endraw %} "

        config_name: "8 IN 4 OUT"
        base_config: "{% raw %} {{ base_config }} {% endraw %} "
              
        # Video Stuff
        video_standard: "{% raw %} {{ video_standard }} {% endraw %} "
        video_resolution: "{% raw %} {{ video_resolution }} {% endraw %} "
        video_bitrate: "{% raw %} {{ video_bitrate }} {% endraw %} "
        video_interface: "{% raw %} {{ video_interface }} {% endraw %} "
        video_codec: "{% raw %} {{ video_codec }} {% endraw %} "
        video_genlock: "{% raw %} {{ video_genlock }} {% endraw %} "
        # Proxy Settings
        proxy: "{% raw %} {{ proxy }} {% endraw %} "
        proxy_codec: "{% raw %} {{ proxy_codec }} {% endraw %} "
        proxy_bitrate: "{% raw %} {{ proxy_bitrate }} {% endraw %} "
        
        # Number of Channels
        record_channels: 8
        ssmo_1_speed: "2x"
        ssmo_1_count: 0
        ssmo_2_speed: "2x"
        ssmo_2_count: 0
        play_channels: 4
        
        # Audio Stuff
        audio_madi: "{% raw %} {{ audio_madi }} {% endraw %} "
        audio_analog: "{% raw %} {{ audio_analog }} {% endraw %} "
        audio_digital: "{% raw %} {{ audio_digital }} {% endraw %} "
        audio_monos: "{% raw %} {{ audio_monos }} {% endraw %} "

        # Control Settings
        rs422_1: "{% raw %} {{ rs422_1 }} {% endraw %} "
        rs422_2: "{% raw %} {{ rs422_2 }} {% endraw %} "
        rs422_3: "{% raw %} {{ rs422_3 }} {% endraw %} "
        rs422_4: "{% raw %} {{ rs422_4 }} {% endraw %} "
        rs422_5: "{% raw %} {{ rs422_5 }} {% endraw %} "
        rs422_6: "{% raw %} {{ rs422_6 }} {% endraw %} "
        lsm_via: "{% raw %} {{ lsm_via }} {% endraw %} "

        # Record Channels Naming and information
        in_channel_1:
          name: "{% raw %} {{ in_channel_1_name }} {% endraw %} "
        in_channel_2:
          name: "{% raw %} {{ in_channel_2_name }} {% endraw %} "
        in_channel_3:
          name: "{% raw %} {{ in_channel_3_name }} {% endraw %} "
        in_channel_4:
          name: "{% raw %} {{ in_channel_4_name }} {% endraw %} "
        in_channel_5:
          name: "{% raw %} {{ in_channel_5_name }} {% endraw %} "
        in_channel_6:
          name: "{% raw %} {{ in_channel_6_name }} {% endraw %} "
        in_channel_7:
          name: "{% raw %} {{ in_channel_7_name }} {% endraw %} "
        in_channel_8:
          name: "{% raw %} {{ in_channel_8_name }} {% endraw %} "
        in_channel_9:
          name: "{% raw %} {{ in_channel_9_name }} {% endraw %} "
        in_channel_10:
          name: "{% raw %} {{ in_channel_10_name }} {% endraw %} "
        in_channel_11:
          name: "{% raw %} {{ in_channel_11_name }} {% endraw %} "
        in_channel_12:
          name: "{% raw %} {{ in_channel_12_name }} {% endraw %} "
        

        # Output Channel Information
        out_channel_1:
          name: "{% raw %} {{ out_channel_1_name }} {% endraw %} "
          primary_control: "{% raw %} {{ out_primary_control }} {% endraw %} "
          secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %} "
          smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %} "
        out_channel_2:
          name: "{% raw %} {{ out_channel_2_name }} {% endraw %} "
          primary_control: "{% raw %} {{ out_primary_control }} {% endraw %} "
          secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %} "
          smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %} "
        out_channel_3:
          name: "{% raw %} {{ out_channel_3_name }} {% endraw %} "
          primary_control: "{% raw %} {{ out_primary_control }} {% endraw %} "
          secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %} "
          smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %} "
        out_channel_4:
          name: "{% raw %} {{ out_channel_4_name }} {% endraw %} "
          primary_control: "{% raw %} {{ out_primary_control }} {% endraw %} "
          secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %} "
          smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %} "
        out_channel_5:
          name: "{% raw %} {{ out_channel_5_name }} {% endraw %} "
          primary_control: "{% raw %} {{ out_primary_control }} {% endraw %} "
          secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %} "
          smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %} "
        out_channel_6:
          name: "{% raw %} {{ out_channel_6_name }} {% endraw %} "
          primary_control: "{% raw %} {{ out_primary_control }} {% endraw %} "
          secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %} "
          smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %} "
    

        xnet_operation: "{% raw %} {{ xnet_operation }} {% endraw %} "
        xnet_name: "{% raw %} {{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', 'EVS \\1') }} {% endraw %} "
        xnet_number: "{% raw %} {{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') | int }} {% endraw %} "
        xnet_visibility: "{% raw %} {{ xnet_visibility }} {% endraw %} "
        xnet_server: "{% raw %} {{ xnet_server }} {% endraw %} "

        gigabit_connection: "{% raw %} {{ gigabit_connection }} {% endraw %} "
        gigabit_link_agg: "{% raw %} {{ gigabit_link_agg }} {% endraw %} "

        media_ip: "{% raw %} {{ inventory_hostname | regex_replace('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{0,3})$', '\\1.\\2.13.\\4') }} {% endraw %} "
        media_gateway: "{% raw %} {{ inventory_hostname | regex_replace('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{0,3})$', '\\1.\\2.13.1') }} {% endraw %} "
        media_subnet: 255.255.255.0

        mv_output_format: "{% raw %} {{ mv_output_format }} {% endraw %} "

        tally_protocol: "{% raw %} {{ tally_protocol }} {% endraw %} "
        tally_display_index: "{% raw %} {{ tally_display_index }} {% endraw %} "

        clip_edit_by_network: "{% raw %} {{ clip_edit_by_network }} {% endraw %} "

        network_copy_push: "{% raw %} {{ network_copy_push }} {% endraw %} "
        ```