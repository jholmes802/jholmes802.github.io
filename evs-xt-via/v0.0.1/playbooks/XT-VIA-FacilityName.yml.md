# XT-VIA-FacilityName.yml

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
    - name: Set Facility Name
      ansible.builtin.uri:
        url: http://{% raw %} {{ inventory_hostname }} {% endraw %} /cfgweb/CfgWeb.dll/FacilityNameJS?SessionID=Reset&FacilityName={% raw %} {{ facilityName | string }} {% endraw %} 
        method: POST
        return_content: yes
      delegate_to: 127.0.0.1
      register: _result
      until: _result.json.FacilityName == '{% raw %} {{ facilityName | string }} {% endraw %} '
      retries: 5
      delay: 5
      when: true

    - name: Print Result
      ansible.builtin.debug:
        msg: "{% raw %} {{ _result }} {% endraw %} "
```
