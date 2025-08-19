# XT-VIA-PB.yml
```yaml
- name: XT-VIA Send Config Lines
  hosts: xt-via
  remote_user: root
  gather_facts: false

  vars:
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
    - name: Send NMOS RDS Registry
      ansible.builtin.command: curl --user evsData:evs! -T ./nmos_node_options.json ftp://{% raw %} {{ inventory_hostname }} {% endraw %} /user/
      delegate_to: 127.0.0.1
      when: true

    - name: Load Version info
      ansible.builtin.slurp:
        src: /mnt/SYS/Versions/current/Version.json
      register: version_info
      when: false

    #    - name: Load Version Info into Facts
    #      ansible.builtin.set_fact:
    #        xtVersion: "{% raw %} {{ version_info.content | b64decode | from_json | json_query('version') }} {% endraw %} "
    #      when: false

    #    - name: Dump xtVersion
    #      ansible.builtin.debug:
    #        msg: "{% raw %} {{ xtVersion }} {% endraw %} "
    #      when: false

    - name: Send Updated Version
      ansible.builtin.copy:
        src: "{% raw %} {{ currentVersionFile }} {% endraw %} "
        dest: /mnt/SYS/Packages/
        owner: root
        group: root
        mode: "775" # -rwxrwxr-x
      when: xtVersion != currentVersion and updateVersion

    - name: Install Updated Version
      command:
        chdir: /mnt/SYS/Versions/current
        cmd: ./Install.sh /mnt/SYS/Packages/Multicam_{% raw %} {{ currentVersionName }} {% endraw %} .tar.gz "Multicam" "{% raw %} {{ currentVersionName }} {% endraw %} " /mnt/SYS/Versions
      when: xtVersion != currentVersion and updateVersion

    - name: Get Server Number
      ansible.builtin.debug:
        msg: "{% raw %} {{ serverNumber }} {% endraw %} "

    - name: Load Config Lines via Copy
      copy:
        src: configLines/{% raw %} {{ item }} {% endraw %} 
        dest: /mnt/APPS/data/setup/{% raw %} {{ item }} {% endraw %} 
        owner: evs
        group: evs
        mode: "775" # -rwxrwxr-x
      loop:
        - cfg00001.lin
        - cfg00002.lin
        - cfg00003.lin
        - cfg00004.lin
        - cfg00005.lin
        - cfg00006.lin
        - cfg00007.lin
        - cfg00008.lin
        - cfg00009.lin
        - cfg00010.lin
        - cfg00011.lin
        - cfg00012.lin
        - cfg00013.lin
        - cfg00014.lin
        - cfg00015.lin
        - cfg00016.lin
      when: false

    - name: Send ConfigLines via Curl
      ansible.builtin.command: curl --location 'http://{% raw %} {{ inventory_hostname }} {% endraw %} /cfgweb/CfgWeb.dll/ImportLineHTML' --form 'TargetNumLine="{% raw %} {{ item | string }} {% endraw %} "' --form 'ConfigFile=@"./configLines/cfg000{% raw %} {{ "{:02}".format(item) }} {% endraw %} .lin"'
      delegate_to: 127.0.0.1
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      when: true

    - name: Create and Send Live IPs
      ansible.builtin.command: python3 ./evsLiveIP.py --serverIP={% raw %} {{ inventory_hostname }} {% endraw %}  --mcVersion={% raw %} {{ xtVersion }} {% endraw %}  --operation=send --configLineNumber={% raw %} {{ item }} {% endraw %} 
      delegate_to: 127.0.0.1
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      when: true

    - name: Set XNET Name and Number by server Number
      ansible.builtin.uri:
        url: http://{% raw %} {{ inventory_hostname }} {% endraw %} /cfgweb/CfgWeb.dll/SetConfigValuesJS?SessionID=Reset&Commit=true&Save=true&NumLine={% raw %} {{ item | string }} {% endraw %} &CFG_PARAM_NET_HOST_NAME=EVS{% raw %} {{ serverNumber | string }} {% endraw %} &CFG_PARAM_NET_NUMBER={% raw %} {{ serverNumber | string | int | string }} {% endraw %} 
        method: POST
      delegate_to: 127.0.0.1
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      when: true

    - name: Set XNET Server Perferred by variable
      ansible.builtin.uri:
        url: http://{% raw %} {{ inventory_hostname }} {% endraw %} /cfgweb/CfgWeb.dll/SetConfigValuesJS?SessionID=Reset&Commit=true&Save=true&NumLine={% raw %} {{ item | string }} {% endraw %} &CFG_PARAM_NET_SERVER=1
        method: POST
        return_content: true
      register: perferredResponse
      delegate_to: 127.0.0.1
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      when: true and perferedServerNumber == ( serverNumber | string | int )

    - name: Set XNET Server Allowed by prefered variable
      ansible.builtin.uri:
        url: http://{% raw %} {{ inventory_hostname }} {% endraw %} /cfgweb/CfgWeb.dll/SetConfigValuesJS?SessionID=Reset&Commit=true&Save=true&NumLine={% raw %} {{ item | string }} {% endraw %} &CFG_PARAM_NET_SERVER=0
        method: POST
        return_content: true
      register: allowedResponse
      delegate_to: 127.0.0.1
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      when: true and perferedServerNumber != ( serverNumber | string | int )

    - name: Set XNET Server Forbidden by variable
      ansible.builtin.uri:
        url: http://{% raw %} {{ inventory_hostname }} {% endraw %} /cfgweb/CfgWeb.dll/SetConfigValuesJS?SessionID=Reset&Commit=true&Save=true&NumLine={% raw %} {{ item | string }} {% endraw %} &CFG_PARAM_NET_SERVER=2
        method: POST
      delegate_to: 127.0.0.1
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      when: false

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

    - name: Set QSFP 29 IP
      # If needed this is the Regex to reverse the IP: regex_replace('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{0,3})$', '\\4.\\3.\\2.\\1') | ansible.utils.ipaddr('int')
      ansible.builtin.uri:
        url: http://{% raw %} {{ inventory_hostname }} {% endraw %} /cfgweb/CfgWeb.dll/SetConfigValuesJS?SessionID=Reset&Commit=true&Save=true&NumLine={% raw %} {{ item | string }} {% endraw %} &CFG_PARAM_NETWORK_QSFP_MODULE1_PORT1_IPADDRESS={% raw %} {{ ('1' + (serverNumber | string) + '.113.' + (truckOctet | string) + '.10') | ansible.utils.ipaddr('int') }} {% endraw %} &CFG_PARAM_NETWORK_QSFP_MODULE1_PORT1_DEFGATEWAY={% raw %} {{ ('1.113.' + (truckOctet | string) + '.10') | ansible.utils.ipaddr('int') }} {% endraw %} 
        method: POST
      delegate_to: 127.0.0.1
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      when: true

    - name: Set QSFP 30 IP
      # If needed this is the Regex to reverse the IP: regex_replace('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{0,3})$', '\\4.\\3.\\2.\\1') | ansible.utils.ipaddr('int')
      ansible.builtin.uri:
        url: http://{% raw %} {{ inventory_hostname }} {% endraw %} /cfgweb/CfgWeb.dll/SetConfigValuesJS?SessionID=Reset&Commit=true&Save=true&NumLine={% raw %} {{ item | string }} {% endraw %} &CFG_PARAM_NETWORK_QSFP_MODULE1_PORT2_IPADDRESS={% raw %} {{ ('1' + (serverNumber | string) + '.213.' + (truckOctet | string) + '.10') | ansible.utils.ipaddr('int') }} {% endraw %} &CFG_PARAM_NETWORK_QSFP_MODULE1_PORT2_DEFGATEWAY={% raw %} {{ ('1.213.' + (truckOctet | string) + '.10') | ansible.utils.ipaddr('int') }} {% endraw %} 
        method: POST
      delegate_to: 127.0.0.1
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      when: true

    - name: Set Media Network IP
      # If needed this is the Regex to reverse the IP: regex_replace('^([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{0,3})$', '\\4.\\3.\\2.\\1') | ansible.utils.ipaddr('int')
      ansible.builtin.uri:
        url: http://{% raw %} {{ inventory_hostname }} {% endraw %} /cfgweb/CfgWeb.dll/SetConfigValuesJS?SessionID=Reset&Commit=true&Save=true&NumLine={% raw %} {{ item | string }} {% endraw %} &CFG_PARAM_EDIT_GBE1_IP_ADDRESS={% raw %} {{ ('1' + (serverNumber | string) + '.13.' + (truckOctet | string) + '.10') | ansible.utils.ipaddr('int') }} {% endraw %} &CFG_PARAM_EDIT_GBE1_GATEWAY_ADDRESS={% raw %} {{ ('1.13.' + (truckOctet | string) + '.10') | ansible.utils.ipaddr('int') }} {% endraw %} 
        method: POST
      delegate_to: 127.0.0.1
      loop: "{% raw %} {{ range(1, 17) | list }} {% endraw %} "
      when: true
```