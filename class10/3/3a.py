#!/usr/bin/env python
from my_devices import my_devices_list
from my_functions import ssh_command, ssh_command2
from netmiko import ConnectHandler
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, wait

start_time = datetime.now()

max_threads = len(my_devices_list)
# print(max_threads)

pool = ThreadPoolExecutor(max_threads)
future_list = []

for my_device in my_devices_list:
   future = pool.submit(ssh_command2, my_device, "show version")
   future_list.append(future)

# waits until all threads are done
wait(future_list)

for future in future_list:
   print("Result: " + future.result())

end_time = datetime.now()
print("Time spent: " + str(end_time - start_time))
