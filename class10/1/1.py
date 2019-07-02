#!/usr/bin/env python
from my_devices import my_devices_list
from netmiko import ConnectHandler
from datetime import datetime


def ssh_command(my_device_dict, show_command):
   my_conn = ConnectHandler(**my_device_dict)
   output = my_conn.send_command(show_command)
   my_conn.disconnect()
   return output

start_time = datetime.now()

for my_device in my_devices_list:
   print(ssh_command(my_device, "show version"))

end_time = datetime.now()
print("Time spent: " + str(end_time - start_time))
