#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

devpass = getpass()

## export NET_TEXTFSM="MYHOME/ntc-templates/templates/"

cisco4 = { "host":'cisco4.lasthop.io',
          "username" : 'pyclass',
          "password" : devpass,
          "device_type" : "cisco_ios",
          "session_log" : "cisco4_session.log" }


nm = ConnectHandler(**cisco4)

output = nm.send_command("show version", use_textfsm=True)
print(output)
print("\n")

output = nm.send_command("show lldp neighbors", use_textfsm=True)
print(output)
pprint(output)

nm.disconnect()
