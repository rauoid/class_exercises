#!/usr/bin/env python
from my_devices import my_devices_list
from my_functions import ssh_command
from netmiko import ConnectHandler
from datetime import datetime
import threading


start_time = datetime.now()

for my_device in my_devices_list:
   my_thread = threading.Thread(target=ssh_command, args=(my_device, "show version",))
   my_thread.start()   

main_thread = threading.currentThread()
for some_thread in threading.enumerate():
   if some_thread != main_thread:
#      print(some_thread)
      some_thread.join()

end_time = datetime.now()
print("Time spent: " + str(end_time - start_time))
