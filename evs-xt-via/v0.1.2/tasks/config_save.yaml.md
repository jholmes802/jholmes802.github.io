```yaml
{% raw %}
- name: Save config
  evs_config_save:
    server_ip: "{{ ansible_host }}"
    session_id: "{{ evs_facts.session_id }}"
    line_number: "{{ config_line_number }}"
{% endraw %}
```