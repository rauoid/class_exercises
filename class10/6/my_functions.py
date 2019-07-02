#!/usr/bin/env python
from netmiko import ConnectHandler
from datetime import datetime

def ssh_command(my_device_dict, show_command):
   my_conn = ConnectHandler(**my_device_dict)
   output = my_conn.send_command(show_command)
   print(output)
   my_conn.disconnect()

def ssh_command2(my_device_dict, show_command):
   my_conn = ConnectHandler(**my_device_dict)
   output = my_conn.send_command(show_command)
   my_conn.disconnect()
   return output

def ssh_command_map(my_device_dict):
   show_command = my_device_dict.pop("show_command")
   my_conn = ConnectHandler(**my_device_dict)
   output = my_conn.send_command(show_command)
   my_conn.disconnect()
   return output

