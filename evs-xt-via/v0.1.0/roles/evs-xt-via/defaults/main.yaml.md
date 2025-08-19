# defaults/main.yaml
```yaml
showname: test-show
multicam_version: "20.07.39"
truck_name: "SHOP"
truck_unit: "A"

all_configLines_enabled: true

base_config: "Multicam LSM"

video_standard: "59.94Hz"
video_resolution: "1080p"
video_codec: "XAVC-Intra 100 (10b)"
video_bitrate: "222"
video_interface: "3G Level-A"
video_genlock: "Genlock SDI"

proxy: true
proxy_codec: "h.264"
proxy_bitrate: 2

audio_madi: "128/128"
audio_analog: None
audio_digital: "16/16"
audio_monos: "16 monos"

rs422_1: "EVS Remote"
rs422_2: "EVS Remote"
rs422_3: "EVS Remote"
rs422_4: "--------"
rs422_5: "--------"
rs422_6: "--------"
lsm_via: "Enabled"

smpte_334M_encoding: "Enabled"

out_secondary_control: "--------"
out_primary_control: "EVS Remote"

xnet_operation: "XNet-VIA"
xnet_name: "EVS"
xnet_visibility: "XNet"
xnet_server: "Allowed"

gigabit_connection: "None" # This should be 10Gbe, 1Gbe
gigabit_link_agg: "None" # This should be LACP

mv_output_format: "1080p"

in_channel_1_name: "CAM 1"
in_channel_2_name: "CAM 2"
in_channel_3_name: "CAM 3"
in_channel_4_name: "CAM 4"
in_channel_5_name: "CAM 5"
in_channel_6_name: "CAM 6"
in_channel_7_name: "CAM 7"
in_channel_8_name: "CAM 8"
in_channel_9_name: "CAM 9"
in_channel_10_name: "CAM 10"
in_channel_11_name: "CAM 11"
in_channel_12_name: "CAM 12"

out_channel_1_name: "PGM 1"
out_channel_2_name: "PGM 2"
out_channel_3_name: "PGM 3"
out_channel_4_name: "PGM 4"
out_channel_5_name: "PGM 5"
out_channel_6_name: "PGM 6"

tally_protocol: "TSL 5.0"
tally_display_index: 10

clip_edit_by_network: true

network_copy_push: "XNet"
```
