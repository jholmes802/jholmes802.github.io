```yaml
---
    - name: Slurp Config Lines
      get_url:
        url: "ftp://evsData:evs!@{% raw %} {{ ansible_host }} {% endraw %} /setup/cfg000{% raw %} {{ '{:02}'.format(item) }} {% endraw %} .lin"
        dest: "{% raw %} {{ config_line_path }} {% endraw %} "
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      delegate_to: 127.0.0.1
      ignore_errors: true

    - name: Slurp Live IP Configs
      get_url:
        url: "ftp://evsData:evs!@{% raw %} {{ ansible_host }} {% endraw %} /setup/IPConfiguration{% raw %} {{ item | string }} {% endraw %} .cfg"
        dest: "{% raw %} {{ liveip_path }} {% endraw %} "
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      delegate_to: 127.0.0.1
      ignore_errors: true

    - name: Get Options JSON
      get_url:
        url: "ftp://evsData:evs!@{% raw %} {{ ansible_host }} {% endraw %} /user/options.json"
        dest: "{% raw %} {{ options_path }} {% endraw %} "
      delegate_to: 127.0.0.1
      ignore_errors: true

    - name: Get NMOS UUIDs
      get_url:
        url: "ftp://evsData:evs!@{% raw %} {{ ansible_host }} {% endraw %} /NMOS/NMOS_Resource_Uuids.txt"
        dest: "{% raw %} {{ nmos_path }} {% endraw %} "
      delegate_to: 127.0.0.1
      ignore_errors: true

    - name: Get NMOS RDS Config
      get_url:
        url: "ftp://evsData:evs!@{% raw %} {{ ansible_host }} {% endraw %} /user/nmos_node_options.json"
        dest: "{% raw %} {{ nmos_path }} {% endraw %} "
      delegate_to: 127.0.0.1
      ignore_errors: true
```