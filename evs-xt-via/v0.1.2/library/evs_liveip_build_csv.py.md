# evs_liveip_build_csv.py

```python
#! .venv/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
import json, os, csv
__metaclass__ = type

# from .evsApi import xtvia
from ..module_utils.liveIPBuild import buildLiveIPcsv

from ansible.module_utils.basic import AnsibleModule

ansible_facts: dict

def run_module():

    arg_spec = dict(server_ip=dict(type="str", required=True),
                    liveip_data_path=dict(type="str", required=True),
                    num_in=dict(type="int", required=True),
                    num_out=dict(type="int", required=True),
                    slsm1=dict(type="int", required=True),
                    slsm2=dict(type="int", required=True),
                    slsm1spd=dict(type="str", required=True),
                    slsm2spd=dict(type="str", required=True),
                    version=dict(type="str", required=True),
                    output_path=dict(type="str", required=True),
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
            current_file = csv.reader(fh.readlines())
            current_file = list(current_file)
    else:
        current_file = []
    with open(module.params["liveip_data_path"], "r") as fh:
        liveip_json = json.load(fh)

    csv_output = buildLiveIPcsv(
        serverIP=module.params["server_ip"],
        numIn=module.params["num_in"],
        numOut=module.params["num_out"],
        slsm1=module.params["slsm1"],
        slsm2=module.params["slsm2"],
        slsm1spd=module.params["slsm1spd"],
        slsm2spd=module.params["slsm2spd"],
        version=module.params["version"],
        workSheetData=liveip_json
        )

    for i in range(0,min(len(current_file), len(csv_output))):
        if current_file[i] != csv_output[i]:
            changed = True
            break

    if not module.check_mode:
        finalWriter = csv.writer(open(module.params["output_path"], "w"), quoting=csv.QUOTE_MINIMAL)
        finalWriter.writerows(csv_output)

    result = dict(changed=changed)
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
```