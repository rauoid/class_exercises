#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass


nxospw = getpass()

nxos1 = { "host":'nxos1.lasthop.io',
          "username" : 'pyclass',
          "password" : nxospw,
          "device_type" : "cisco_nxos" }

nxos2 = { "host":'nxos2.lasthop.io',
          "username" : 'pyclass',
          "password" : nxospw,
          "device_type" : "cisco_nxos" }

nxosdevs = [ nxos1, nxos2 ]

for nxdev in nxosdevs:
   nm = ConnectHandler(**nxdev)
   print(nm.find_prompt())
