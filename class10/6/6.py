#!/usr/bin/env python
from my_devices import my_devices_list
from my_functions import ssh_command, ssh_command2, ssh_command_map
from netmiko import ConnectHandler
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed

start_time = datetime.now()

# build a list for map() method with command in it
my_devices_list_w_cmd = []

for my_device in my_devices_list:
   if my_device['device_type'] == "juniper_junos":
      my_device['show_command'] = "show arp"
      my_devices_list_w_cmd.append(my_device)
   else:
     my_device['show_command'] = "show ip arp"
     my_devices_list_w_cmd.append(my_device)

max_processes = len(my_devices_list)
# print(max_processes)

# with context manager
with ProcessPoolExecutor(max_processes) as pool:
   results_generator = pool.map(ssh_command_map, my_devices_list_w_cmd)

   for result in results_generator:
      print(result)

end_time = datetime.now()
print("Time spent: " + str(end_time - start_time))
