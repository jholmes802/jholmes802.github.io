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
    )
    # seed the result dict in the object
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    # This builds the server object and tells it to do minimal inspection
    via = xtvia.xtviaServer(
        module.params["server_ip"],
        [module.params["line_number"]],
        inspection=2,
        sessionID=module.params["session_id"],
    )

    via._save(numLine=module.params["line_number"], save=True)
    # Our result back to Ansible.
    result = dict(
        changed=True,
    )

    # Only Updates the paramter if we are not just checking it.
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
