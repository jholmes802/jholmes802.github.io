#! .venv/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ..module_utils.evsApi import xtvia
from ..module_utils.evsApi.liveIP import *

import json

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r"""
#

"""


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        server_ip=dict(type="str", required=True),
        session_id=dict(type="str", required=False, default="Reset"),
        line_number=dict(type="int", required=True),
        uri=dict(type='str', rquired=True),
        value=dict(type="str", required=True),
    )

    # channel_direction is going to be expecting on of the following ["inputs", "outputs", "mv_inputs", "mv_outputs"]

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # Going to checkout Things.
    via = xtvia.xtviaServer(
        module.params["server_ip"],
        [module.params["line_number"]],
        inspection=2,
        getLiveIPs=True,
    )
    liveIP = via._get_liveip_one(module.params["line_number"], module.params["uri"])

    curVal = liveIP["Value"]
    changed = curVal == module.params["value"]

    if not module.check_mode:
        response: dict = via._set_liveip_one(module.params["line_number"], module.params["uri"], module.params["value"])

    result = dict(changed=changed, current_value=curVal, intended_value=module.params["value"])
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
