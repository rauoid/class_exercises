#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass


devpass = getpass()

cisco4 = { "host":'cisco4.lasthop.io',
          "username" : 'pyclass',
          "password" : devpass,
          "device_type" : "cisco_ios",
          "session_log" : "cisco4_session_b.log" }


nm = ConnectHandler(**cisco4)

nm.send_command("ping", expect_string=r'Protocol')
nm.send_command("\n", expect_string=r'Target')
nm.send_command("8.8.8.8", expect_string=r'Repeat')
nm.send_command("\n", expect_string=r'Datagram')
nm.send_command("\n", expect_string=r'Timeout')
nm.send_command("\n", expect_string=r'Extended')
nm.send_command("\n", expect_string=r'Sweep')


nm.disconnect()
