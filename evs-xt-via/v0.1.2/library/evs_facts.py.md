# evs_facts.py
```python
#! .venv/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

# from .evsApi import xtvia
from ..module_utils.evsApi import xtvia

from ansible.module_utils.basic import AnsibleModule

ansible_facts: dict


def getFacts(serverIP: str) -> dict:
    via = xtvia.xtviaServer(serverIP, inspection=2)
    result = {
        "PC_LAN_1": via.get_serverIP(),
        "Chassis": via.get_chassis(),
        "HardwareVersion": via.get_HWEdition(),
        "MCVersion": via.get_version(),
        "SerialNumber": via.get_SN(),
        "FacilityName": via.get_facility_name(),
        "session_id": via._get_SessionID(),
    }
    return result


def run_module():

    arg_spec = dict(server_ip=dict(type="str", required=True))
    result = dict(changed=False)

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(argument_spec=arg_spec, supports_check_mode=True)

    # Going to checkout Things.

    facts = getFacts(serverIP=module.params["server_ip"])

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**facts)


def main():
    run_module()


if __name__ == "__main__":
    main()
```