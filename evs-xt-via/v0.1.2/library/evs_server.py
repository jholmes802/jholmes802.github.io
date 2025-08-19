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
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # This builds the server object and tells it to do minimal inspection
    via = xtvia.xtviaServer(
        module.params["server_ip"],
        inspection=2,
        sessionID=module.params["session_id"],
    )
    # We can see if the facility name matches the one passed in or not here.
    result = dict(changed=(via.get_facility_name() != module.params["facility_name"]))

    # Only updates the facility name if we are not in check mode
    if module.check_mode:
        module.exit_json(**result)
    else:
        via.set_facility_name(module.params["facility_name"])
        module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
