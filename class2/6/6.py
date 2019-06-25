#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
import time

devpass = getpass()

cisco4 = { "host":'cisco4.lasthop.io',
          "username" : 'pyclass',
          "password" : devpass,
          "secret" : devpass,
          "device_type" : "cisco_ios",
          "session_log" : "cisco4_session.log" }


nm = ConnectHandler(**cisco4)

# a
output = nm.find_prompt()
print(output)
print("\n")

# b
nm.config_mode()
output = nm.find_prompt()
print(output)
print("\n")

# c
nm.exit_config_mode()
output = nm.find_prompt()
print(output)
print("\n")

# d
nm.write_channel("disable\n")
# e
time.sleep(3)

# f
nm.enable()
output = nm.find_prompt()
print(output)
print("\n")

nm.disconnect()
