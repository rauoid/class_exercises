#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass


nxospw = getpass()

nxos1 = { "host":'nxos1.lasthop.io',
          "username" : 'pyclass',
          "password" : nxospw,
          "device_type" : "cisco_nxos" }


nm = ConnectHandler(**nxos1)
print(nm.find_prompt())
