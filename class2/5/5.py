#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass


nxospw = getpass()

vlans_config_file="5_vlans_config.txt"

nxos1 = { "host":'nxos1.lasthop.io',
          "username" : 'pyclass',
          "password" : nxospw,
          "device_type" : "cisco_nxos",
          "session_log" : "nxos1_session.log"
         }

nxos2 = { "host":'nxos2.lasthop.io',
          "username" : 'pyclass',
          "password" : nxospw,
          "device_type" : "cisco_nxos",
          "session_log" : "nxos2_session.log"
 }

nxosdevs = [ nxos1, nxos2 ]

for nxdev in nxosdevs:
   print(nxdev['host'])
   nm = ConnectHandler(**nxdev)
   # send vlan config
   output=nm.send_config_from_file(config_file=vlans_config_file)
   # save config
   output+=nm.save_config()
   #
   nm.disconnect()
   print(output)
   print("/n")
