```yaml
{% raw %}
---
    - name: Slurp Config Lines
      get_url:
        url: "ftp://evsData:evs!@{{ ansible_host }}/setup/cfg000{{ '{:02}'.format(item) }}.lin"
        dest: "{{ config_line_path }}"
      loop: "{{ range(1, 17) | list }}"
      delegate_to: 127.0.0.1
      ignore_errors: true

    - name: Slurp Live IP Configs
      get_url:
        url: "ftp://evsData:evs!@{{ ansible_host }}/setup/IPConfiguration{{ item | string }}.cfg"
        dest: "{{ liveip_path }}"
      loop: "{{ range(1, 17) | list }}"
      delegate_to: 127.0.0.1
      ignore_errors: true

    - name: Get Options JSON
      get_url:
        url: "ftp://evsData:evs!@{{ ansible_host }}/user/options.json"
        dest: "{{ options_path }}"
      delegate_to: 127.0.0.1
      ignore_errors: true

    - name: Get NMOS UUIDs
      get_url:
        url: "ftp://evsData:evs!@{{ ansible_host }}/NMOS/NMOS_Resource_Uuids.txt"
        dest: "{{ nmos_path }}"
      delegate_to: 127.0.0.1
      ignore_errors: true

    - name: Get NMOS RDS Config
      get_url:
        url: "ftp://evsData:evs!@{{ ansible_host }}/user/nmos_node_options.json"
        dest: "{{ nmos_path }}"
      delegate_to: 127.0.0.1
      ignore_errors: true
{% endraw %}
```