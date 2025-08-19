# XT-VIA-LiveIs.yml

```yaml
{% raw %}
- name: XT-VIA Send Config Lines
  hosts: xt-via
  remote_user: root
  gather_facts: false

  vars:
    ansible_ssh_pass: evs!
    ansible_ssh_user: root
    serverNumber: "{{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') }}"
    facilityName: "{{  'GCV-[TRUCK]-A-EVS-' + serverNumber }}"
    currentVersion: "21.00.21"
    currentVersionFile: "./software/Multicam_20_07_35/Multicam_20.07.35.84415.tar.gz"
    currentVersionName: "20.00.21.84415"
    updateVersion: false
    perferedServerNumber: 1
    truckOctet: 64
    xtVersion: "21.00.21"
  tasks:
    - name: Build Live IP CSV
      ansible.builtin.command: python3 ./evsLiveIP.py --serverIP={{ inventory_hostname }} --mcVersion={{ xtVersion }} --operation=build --configLineNumber={{ item }}
      delegate_to: 127.0.0.1
      loop: "{{ range(1, 17) | list }}"
      when: true

    - name: Create and Send Live IPs
      ansible.builtin.command: python3 ./evsLiveIP.py --serverIP={{ inventory_hostname }} --mcVersion={{ xtVersion }} --operation=send --configLineNumber={{ item }}
      delegate_to: 127.0.0.1
      loop: "{{ range(1, 17) | list }}"
      when: true
{% endraw %}
```