```yaml
---
- name: Configure Base Config
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_QS_HD_OUTPUT_FORMAT"
    config_value: "{% raw %} {{ mv_output_format }} {% endraw %} "
  # loop: "{% raw %} {{ serverVars.config_lines }} {% endraw %} "

- name: Configure MV Channels MV 1
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "{% raw %} {{ item }} {% endraw %} "
    config_value: "None        "
  when: play_channels == 0
  loop:
    - CFG_PARAM_QS_GRIDVALUE_1
    - CFG_PARAM_QS_GRIDVALUE_2
    - CFG_PARAM_QS_GRIDVALUE_3
    - CFG_PARAM_QS_GRIDVALUE_4
    - CFG_PARAM_QS2_GRIDVALUE_1
    - CFG_PARAM_QS2_GRIDVALUE_2
    - CFG_PARAM_QS2_GRIDVALUE_3
    - CFG_PARAM_QS2_GRIDVALUE_4
    - CFG_PARAM_QS3_GRIDVALUE_1
    - CFG_PARAM_QS3_GRIDVALUE_2
    - CFG_PARAM_QS3_GRIDVALUE_3
    - CFG_PARAM_QS3_GRIDVALUE_4
    - CFG_PARAM_QS4_GRIDVALUE_1
    - CFG_PARAM_QS4_GRIDVALUE_2
    - CFG_PARAM_QS4_GRIDVALUE_3
    - CFG_PARAM_QS4_GRIDVALUE_4

- name: Configure Audio Monitoring MV 1
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_QS_AUDIOMONITORINGVALUE"
    config_value: "None        "
  when: play_channels == 0

- name: Configure Audio Monitoring MV 2
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_QS2_AUDIOMONITORINGVALUE"
    config_value: "None        "
  when: play_channels == 0

- name: Configure Audio Monitoring MV 3
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_QS3_AUDIOMONITORINGVALUE"
    config_value: "None        "
  when: play_channels == 0

- name: Configure Audio Monitoring MV 4
  evs_config:
    server_ip: "{% raw %} {{ ansible_host }} {% endraw %} "
    session_id: "{% raw %} {{ evs_facts.session_id }} {% endraw %} "
    line_number: "{% raw %} {{ config_line_number }} {% endraw %} "
    config_parameter: "CFG_PARAM_QS4_AUDIOMONITORINGVALUE"
    config_value: "None        "
  when: play_channels == 0

```