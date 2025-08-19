# main.yaml
```yaml
showname: "test-show"
multicam_version: "20.07.39"
system_name: "SHOP"
truck_unit: "A"
config_line_number: 1
config_name: "8 IN 4 OUT"
base_config: "Multicam LSM"
no_fec: false
serverNumber: "{% raw %} {{ ansible_host | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') }} {% endraw %}"
options_path: "{% raw %} {{ inventory_dir }} {% endraw %}/files/evs-configs/evs-{% raw %} {{ serverNumber }} {% endraw %}/options/options.json"
nmos_options_path: "{% raw %} {{ inventory_dir }} {% endraw %}/files/evs-configs/evs-{% raw %} {{ serverNumber }} {% endraw %}/nmos/nmos_node_options.json"
repo_base_path: "{% raw %} {{ inventory_dir }} {% endraw %}/files/evs-configs"

route_xt_via_input: false
ptp_domain: 127
evs:
  audio_g1: "true"
  audio_g2: "true"

video_standard: "59.94Hz"
video_resolution: "1080p"
video_codec: "XAVC-Intra 100 (10b)"
video_bitrate: "222"
video_interface: "XiP"
video_genlock: "Genlock PTP"
video_hdr_profile: "HLG"
video_hdr_color_gamut: "rec.2020"

proxy: "Yes"
proxy_codec: "h.264"
proxy_bitrate: 2

record_channels: 8
ssmo_1_speed: "2x"
ssmo_1_count: 0
ssmo_2_speed: "2x"
ssmo_2_count: 0
play_channels: 4

audio_madi: "128/128"
audio_analog: None
audio_digital: "16/16"
audio_monos: "16 monos"
in_audio_type: "E"
out_audio_type: "E"

rs422_1: "EVS Remote"
rs422_2: "EVS Remote"
rs422_3: "EVS Remote"
rs422_4: "--------"
rs422_5: "--------"
rs422_6: "--------"
lsm_via: "Enabled"

smpte_334M_encoding: "Yes"

out_secondary_control: "--------"
out_primary_control: "EVS Remote"

in_secondary_control: "--------"
in_primary_control: "EVS Remote"

xnet_operation: "XNet-VIA"
xnet_visibility: "XNet"
xnet_server: "Allowed"

gigabit_connection: "10Gbe" # This should be 10Gbe, 1Gbe
gigabit_link_agg: "LACP" # This should be LACP

mv_output_format: "1080p"

in_channel_1:
  name: "CAM 1"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"
in_channel_2:
  name: "CAM 2"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"
in_channel_3:
  name: "CAM 3"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"
in_channel_4:
  name: "CAM 4"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"
in_channel_5:
  name: "CAM 5"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"
in_channel_6:
  name: "CAM 6"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"
in_channel_7:
  name: "CAM 7"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"
in_channel_8:
  name: "CAM 8"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"
in_channel_9:
  name: "CAM 9"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"
in_channel_10:
  name: "CAM 10"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"
in_channel_11:
  name: "CAM 11"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"
in_channel_12:
  name: "CAM 12"
  primary_control: "{% raw %} {{ in_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ in_secondary_control }} {% endraw %}"

mix_one_channel: "Yes"

out_channel_1:
  name: "PGM 1"
  primary_control: "{% raw %} {{ out_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %}"
  smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %}"
  mix_one_channel: "{% raw %} {{ mix_one_channel }} {% endraw %}"
out_channel_2:
  name: "PGM 2"
  primary_control: "{% raw %} {{ out_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %}"
  smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %}"
  mix_one_channel: "{% raw %} {{ mix_one_channel }} {% endraw %}"
out_channel_3:
  name: "PGM 3"
  primary_control: "{% raw %} {{ out_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %}"
  smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %}"
  mix_one_channel: "{% raw %} {{ mix_one_channel }} {% endraw %}"
out_channel_4:
  name: "PGM 4"
  primary_control: "{% raw %} {{ out_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %}"
  smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %}"
  mix_one_channel: "{% raw %} {{ mix_one_channel }} {% endraw %}"
out_channel_5:
  name: "PGM 5"
  primary_control: "{% raw %} {{ out_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %}"
  smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %}"
  mix_one_channel: "{% raw %} {{ mix_one_channel }} {% endraw %}"
out_channel_6:
  name: "PGM 6"
  primary_control: "{% raw %} {{ out_primary_control }} {% endraw %}"
  secondary_control: "{% raw %} {{ out_secondary_control }} {% endraw %}"
  smpte_334M_encoding: "{% raw %} {{ smpte_334M_encoding }} {% endraw %}"
  mix_one_channel: "{% raw %} {{ mix_one_channel }} {% endraw %}"

media_subnet: 255.255.255.0

tally_protocol: "TSL 5.0"
tally_display_index: 10

clip_edit_by_network: "1"

network_copy_push: "XNet"

xnet_name: "{% raw %} {{ ansible_host | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', 'EVS \\1') }} {% endraw %}"
xnet_number: "{% raw %} {{ ansible_host | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') | int }} {% endraw %}"

media_ip: "{% raw %} {{ ansible_host | regex_replace('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{0,3})$', '\\1.\\2.13.\\4') }} {% endraw %}"
media_gateway: "{% raw %} {{ ansible_host | regex_replace('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{0,3})$', '\\1.\\2.13.1') }} {% endraw %}"

truck_number: "{% raw %} {{ ansible_host | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') | int}} {% endraw %}"
facility_name: "GCV-{% raw %} {{ system_name | upper }} {% endraw %}-{% raw %} {{ truck_unit }} {% endraw %}-EVS-{% raw %} {{ ansible_host | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') }} {% endraw %}"

st2110_ip: "{% raw %} {{ ansible_host | regex_replace('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{0,3})$', '\\1.\\2.113.\\4') }} {% endraw %}"
st2110_gateway: "{% raw %} {{ ansible_host | regex_replace('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{0,3})$', '\\1.\\2.113.1') }} {% endraw %}"
st2110_subnet: 255.255.255.0
```