# evs_liveip.py

```python
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
        channel_direction=dict(type="str", required=True),
        channel_number=dict(type="int", required=True),
        phase_number=dict(type="int", required=False),
        channel_type=dict(type="str", required=True),
        parameter=dict(type="str", required=True),
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
    liveIPStruct: LiveIPConfig = via.get_liveip(module.params["line_number"])

    match module.params["channel_direction"]:
        case "inputs":
            channel: Channel = liveIPStruct.getInput(module.params["channel_number"])
        case "outputs":
            channel: Channel = liveIPStruct.getOutput(module.params["channel_number"])
        case "in_mon_outs":
            channel: Channel = liveIPStruct.getInput(module.params["channel_number"])
        case "mv_inputs":
            channel: Channel = liveIPStruct.getMVInput(module.params["channel_number"])
        case "mv_outputs":
            channel: Channel = liveIPStruct.getMVOutput(module.params["channel_number"])

    # We have a handling for the channel object now.
    # Luckily the channel types are nearly identical from our perspective, so this should be easier.
    signal: Media
    match module.params["channel_type"]:
        case "anc":
            signal = channel.get_anc(1)
        case "audio_g1":
            signal = channel.get_audio(1)
        case "audio_g2":
            signal = channel.get_audio(2)
        case "audio_g3":
            signal = channel.get_audio(3)
        case "audio_g4":
            signal = channel.get_audio(4)
        case "video":
            signal = channel.get_video(1)
        case "phase":
            signal = channel.get_phase(module.params["phase_number"])
        case "video_mon":
            signal = channel.get_video_mon(1)
        case "audio_mon_g1":
            signal = channel.get_audio_mon(1)
        case "audio_mon_g2":
            signal = channel.get_audio_mon(2)
        case "audio_mon_g3":
            signal = channel.get_audio_mon(3)
        case "audio_mon_g4":
            signal = channel.get_audio_mon(5)

    # Now we have a signal in the form of the Media class that should have all the standard functions we need.
    # If using redundant we need to do some extra work but here we will just move on.
    stream: Stream = signal.get_stream()
    changed: bool = False

    if module.params["parameter"] in ["dest_port", "destination_port"]:
        curVal = str(stream.get_destinationPort())
        if curVal != str(module.params["value"]):
            changed = True
        if not module.check_mode:
            stream.set_destinationPort(str(module.params["value"]))

    if module.params["parameter"] in ["dest_addr", "dest_address", "destination_address"]:
        curVal = str(stream.get_destinationAddress())
        if curVal != str(module.params["value"]):
            changed = True
        if not module.check_mode:
            stream.set_destinationAddress(str(module.params["value"]))

    if module.params["parameter"] in ["enabled", "enable"]:
        curVal = str(stream.get_enabled()).lower()
        if curVal != str(module.params["value"]).lower():
            changed = True
        if not module.check_mode:
            stream.set_enabled(str(module.params["value"]).lower())


    result = dict(changed=changed, current_value=curVal, intended_value=module.params["value"])
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
```