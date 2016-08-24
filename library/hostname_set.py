#!/usr/bin/python

from ansible.module_utils.basic import *

def get_hostname(module):
    (rc, so, se) = module.run_command('hostname -s')    
    if rc != 0:
        module.fail_json(msg='hostname command failed: %s' % (str(so) + str(se)))
    return so.strip()

def set_hostname(module, hostname):
    changed = False    
    current_name = get_hostname(module)    
    if current_name != hostname:
        changed = True
        cmd = 'hostnamectl set-hostname %s' % hostname
        (rc, so, se) = module.run_command(cmd)
        if rc != 0:
            module.fail_json(msg='hostname command failed: %s' % (str(so) + str(se)))
    return changed

if __name__ == '__main__':
    global module
    module = AnsibleModule(
        argument_spec=dict(
            name = dict(required=True),
        ),
        supports_check_mode=False
    )
    hostname = module.params['name']
    result = {}
    result['changed'] = set_hostname(module, hostname)
    module.exit_json(**result)
