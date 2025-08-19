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
        session_id=dict(type="str", required=False, default="Reset"),
        line_number=dict(type="int", required=False),
        config_parameter=dict(type="str", required=False),
        config_value=dict(type="str", required=False),
    )
    # seed the result dict in the object
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # This builds the server object and tells it to do minimal inspection
    via = xtvia.xtviaServer(
        module.params["server_ip"],
        [module.params["line_number"]],
        inspection=2,
        singleParam=module.params["config_parameter"],
        sessionID=module.params["session_id"],
    )

    # Get the config line information and drill down to the parameter.
    cfgLine = via.get_config(module.params["line_number"])
    cfgParm = cfgLine.get_param(module.params["config_parameter"])

    # This is what tells us if the parameter has changed or not.
    changed = cfgParm.getCurrentLabel() != module.params["config_value"]

    # Our result back to Ansible.
    result = dict(
        changed=changed, current_value=cfgParm.getCurrentValue(), intended_value=module.params["config_value"]
    )

    # Only Updates the paramter if we are not just checking it.
    if module.check_mode:
        module.exit_json(**result)
    else:
        cfgParm.setCurrentValue(module.params["config_value"], )
        module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
