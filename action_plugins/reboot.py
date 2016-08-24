#!/usr/bin/python

import time
from ansible.plugins.action import ActionBase
from pprint import pprint

class ActionModule(ActionBase):
    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=None):
        # let the user define the shutdown command
        executable = self._task.args.get('_raw_params', 
                                         '/usr/sbin/reboot')
        # kill it
        reboot = {}
        try:
            reboot = self._low_level_execute_command(executable)
        except Exception as e:
            # give it a second to actually die
            time.sleep(5)

        # now wait for it to come back up ...
        retries = 0
        running = False
        while not running and retries < 20:
            try:
                self._low_level_execute_command('whoami') 
                running = True
            except:
                retries += 1
                time.sleep(2)

        reboot['changed'] = True
        if not running:
            reboot['failed'] = True
        else:
            reboot['failed'] = False
        return reboot
