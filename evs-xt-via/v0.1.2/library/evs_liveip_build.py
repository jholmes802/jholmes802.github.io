#! .venv/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
import json, os
__metaclass__ = type

# from .evsApi import xtvia
from ..module_utils.liveIPBuild import loadIPJson

from ansible.module_utils.basic import AnsibleModule

ansible_facts: dict

def run_module():

    arg_spec = dict(server_ip=dict(type="str", required=True),
                    output_path=dict(type="str", required=True),
                    multicast_sheet=dict(type="str", required=True)
                    )
    changed=False

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module:AnsibleModule = AnsibleModule(argument_spec=arg_spec, supports_check_mode=True)

    # Going to checkout Things.
    if os.path.isfile(module.params["output_path"]):
        with open(module.params["output_path"], "r") as fh:
            current_file = json.load(fh)
    else:
        current_file = {}
    updated = loadIPJson(serverIP = module.params["server_ip"], liveIPSourceFile = module.params["multicast_sheet"])

    if current_file != updated:
        changed = True

    if not module.check_mode:
        with open(module.params["output_path"], "w") as fh:
            json.dump(updated, fh)

    result = dict(changed=changed)
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
