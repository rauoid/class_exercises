#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

nxospw = getpass()


nxos2_dly_2 = { "host":'nxos2.lasthop.io',
          "username" : 'pyclass',
          "password" : nxospw,
          "device_type" : "cisco_nxos",
          "session_log" : "nxos2_session_2.log",
          "global_delay_factor" : 2
 }

nxos2_dly_8 = { "host":'nxos2.lasthop.io',
          "username" : 'pyclass',
          "password" : nxospw,
          "device_type" : "cisco_nxos",
          "session_log" : "nxos2_session_8.log",
          "global_delay_factor" : 8
 }

### nxos2_dly_2
d_start_2 = datetime.now()
nm = ConnectHandler(**nxos2_dly_2)

output = nm.send_command("show lldp neighbors detail")

print(output)

nm.disconnect()

d_end_2 = datetime.now()

### nxos2_dly_8
d_start_8 = datetime.now()

nm = ConnectHandler(**nxos2_dly_8)

output = nm.send_command("show lldp neighbors detail")

print(output)

nm.disconnect()
d_end_8 = datetime.now()

print("### Results ###")
print("Duration glob dly fctr 2: %s" % (d_end_2-d_start_2))
print("Duration glob dly fctr 8: %s" % (d_end_8-d_start_8))


