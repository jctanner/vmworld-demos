#!/usr/bin/python

from ansible.module_utils.basic import *

if __name__ == '__main__':
    global module
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )

    result={}
    module.exit_json(**result)
