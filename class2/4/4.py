#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

devpass = getpass()

cisco3 = { "host":'cisco3.lasthop.io',
          "username" : 'pyclass',
          "password" : devpass,
          "device_type" : "cisco_ios",
          "fast_cli" : True,
          "session_log" : "cisco3_session.log" }


nm = ConnectHandler(**cisco3)

commands = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]

output = nm.send_config_set(commands)
print(output)

nm.disconnect()
