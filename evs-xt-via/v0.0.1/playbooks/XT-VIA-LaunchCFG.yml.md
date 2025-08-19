# XT-VIA-LaunchCFG.yml


```yaml
# To run this:: ansible-playbook -i inventories/064-Falgship/flahship-a-invInit.yml XT-VIA-LaunchCFG.yml
# This ansible playbook will launch a sepcific configline
- name: XT-VIA Send Config Lines
  hosts: xt-via
  remote_user: root
  gather_facts: false

  vars:
    configLine: 6 #Set this line to the config line number you want to launch
    ansible_ssh_pass: evs!
    ansible_ssh_user: root
  tasks:
    - name: Launch Config Line
      ansible.builtin.uri:
        url: http://{{ inventory_hostname }}/cfgweb/CfgWeb.dll/LaunchConfigJS?NumLine={{ configLine | string }}&SessionID=Reset
        method: POST
        return_content: yes
      delegate_to: 127.0.0.1
      register: _result
      until: _result.json.IsMulsetupRunning or _result.json.IsMulticamRunning
      retries: 3

    - name: Print Result
      ansible.builtin.debug:
        msg: "{{ _result }}"
```