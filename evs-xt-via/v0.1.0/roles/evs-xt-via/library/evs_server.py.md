# library/evs_server.py

```python
#! .venv/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..module_utils.evsApi import xtvia

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r"""
# 

"""


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        server_ip=dict(type="str", required=True),
        facility_name=dict(type="str", required=True),
        session_id=dict(type="str", required=False, default="Reset"),
    )
    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # Going to checkout Things.
    via = xtvia.xtviaServer(
        module.params["server_ip"],
        [],
        inspection=2,
        sessionID=module.params["session_id"],
    )

    result = dict(changed=(via.get_facility_name() != module.params["facility_name"]))

    if module.check_mode:
        module.exit_json(**result)
    else:
        via.set_facility_name(module.params["facility_name"])
        module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
```