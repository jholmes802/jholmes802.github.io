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
        [module.params["line_number"]],
        inspection=2,
        singleParam=module.params["config_parameter"],
        sessionID=module.params["session_id"],
    )

    cfgLine = via.get_config(module.params["line_number"])
    cfgParm = cfgLine.get_param(module.params["config_parameter"])
    module.exit_json(value=cfgParm.getCurrentLabel())


def main():
    run_module()


if __name__ == "__main__":
    main()
