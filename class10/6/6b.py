#!/usr/bin/env python
from my_devices import my_devices_list
from my_functions import ssh_command, ssh_command2
from netmiko import ConnectHandler
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed

start_time = datetime.now()

# build a list for map() method with command in it
cmd_list = []

for my_device in my_devices_list:
   if my_device['device_type'] == "juniper_junos":
     cmd_list.append("show arp")
   else:
     cmd_list.append("show ip arp")

max_processes = len(my_devices_list)
# print(max_processes)

# with context manager
with ProcessPoolExecutor(max_processes) as pool:
   results_generator = pool.map(ssh_command2, my_devices_list, cmd_list)

   for result in results_generator:
      print(result)

end_time = datetime.now()
print("Time spent: " + str(end_time - start_time))
