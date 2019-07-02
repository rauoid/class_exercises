#!/usr/bin/env python
from my_devices import my_devices_list
from my_functions import ssh_command, ssh_command2
from netmiko import ConnectHandler
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed

start_time = datetime.now()

max_processes = len(my_devices_list)
# print(max_processes)

# with content manager
with ProcessPoolExecutor(max_processes) as pool:
   future_list = []

   for my_device in my_devices_list:
      future = pool.submit(ssh_command2, my_device, "show version")
      future_list.append(future)

   # process as thread is completed
   for future in as_completed(future_list):
      print("Result: " + future.result())

end_time = datetime.now()
print("Time spent: " + str(end_time - start_time))
