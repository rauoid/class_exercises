#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass


nxospw = getpass()

nxos1 = { "host":'nxos1.lasthop.io',
          "username" : 'pyclass',
          "password" : nxospw,
          "device_type" : "cisco_nxos",
          "session_log" : "3.log" }


nm = ConnectHandler(**nxos1)

output = nm.send_command("show version")
# print(output)
