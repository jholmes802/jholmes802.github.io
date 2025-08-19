# check_server_info.yaml

```yaml
---

- name: Set Facility Name
  evs_server:
    server_ip: "{{ inventory_hostname }}"
    facility_name: "{{ serverVars.facility_name }}"
    session_id: "{{ evs_facts.session_id }}"

```