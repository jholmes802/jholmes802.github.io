# XT-VIA-LiveIs.yml

```yaml
- name: XT-VIA Send Config Lines
  hosts: xt-via
  remote_user: root
  gather_facts: false

  vars:
    ansible_ssh_pass: evs!
    ansible_ssh_user: root
    serverNumber: "{% raw %} {{ inventory_hostname | regex_replace('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.\\d([0-9]{0,2})$', '\\1') }} {% endraw %} "
    facilityName: "{% raw %} {{  'GCV-[TRUCK]-A-EVS-' + serverNumber }} {% endraw %} "
    currentVersion: "21.00.21"
    currentVersionFile: "./software/Multicam_20_07_35/Multicam_20.07.35.84415.tar.gz"
    currentVersionName: "20.00.21.84415"
    updateVersion: false
    perferedServerNumber: 1
    truckOctet: 64
    xtVersion: "21.00.21"
  tasks:
    - name: Build Live IP CSV
      ansible.builtin.command: python3 ./evsLiveIP.py --serverIP={% raw %} {{ inventory_hostname }} {% endraw %}  --mcVersion={% raw %} {{ xtVersion }} {% endraw %}  --operation=build --configLineNumber={% raw %} {{ item }} {% endraw %} 
      delegate_to: 127.0.0.1
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      when: true

    - name: Create and Send Live IPs
      ansible.builtin.command: python3 ./evsLiveIP.py --serverIP={% raw %} {{ inventory_hostname }} {% endraw %}  --mcVersion={% raw %} {{ xtVersion }} {% endraw %}  --operation=send --configLineNumber={% raw %} {{ item }} {% endraw %} 
      delegate_to: 127.0.0.1
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      when: true
```