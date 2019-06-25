#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass


devpass = getpass()

cisco4 = { "host":'cisco4.lasthop.io',
          "username" : 'pyclass',
          "password" : devpass,
          "device_type" : "cisco_ios",
          "session_log" : "cisco4_session_a.log" }


nm = ConnectHandler(**cisco4)

# output = nm.send_command("show version")
# print(output)

nm.send_command_timing("ping")
# protocol
nm.send_command_timing("\n")
# target address
nm.send_command_timing("8.8.8.8")
# count
nm.send_command_timing("\n")
# datagram size
nm.send_command_timing("\n")
#  timeout
nm.send_command_timing("\n")
# ext commands
nm.send_command_timing("\n")
# sweep range
nm.send_command_timing("\n")



nm.disconnect()
