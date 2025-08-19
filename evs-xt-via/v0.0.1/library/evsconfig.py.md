# evscofing.md

```python

#! /usr/bin/python3
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import json
from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        facilityName=dict(type='str', required=True),
        setLiveIP=dict(type='bool', required=False, default=False),
        configLineNumber=dict(type='int', required=True),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result['original_message'] = module.params['facilityName']
    result['message'] = 'goodbye'

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if module.params['setLiveIP']:
        result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['facilityName'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


class cfgLine:
    def __init__(self, cfgLine):
        self._number: int = cfgLine["Number"]
        self._name: str = cfgLine["CFG_PARAM_CONFIG_NAME"]
        self._loaded: bool = cfgLine["Loaded"]
        self._isValid: bool = cfgLine["Valid"]
        self._cfgParms = dict()

    def setVideoStandard(self, standard):
        self._cfgParms["CFG_PARAM_VIDEO_STANDARD"] = standard.string

    def setVideoResolution(self, resolution):
        self._cfgParms["CFG_PARAM_VIDEO_MODE"] = resolution.string

    def setVideoAspectRatio(self, aspectRatio):
        self._cfgParms["CFG_PARAM_VIDEO_ASPECT_RATIO"] = aspectRatio.string


class cfgParm:
    def __init__(self, cfgParmName, cfgParmVals) -> None:
        self._name = cfgParmName
        self.value = cfgParmVals["Value"]
        self.Text = cfgParmVals["Text"]
        self.Status = cfgParmVals["Status"]

def main():
    run_module()

if __name__ == "__main__":
    main()
```