#!/usr/bin/env python3
from napalm import get_network_driver
from pprint import pprint
from my_devices import cisco3, arista1

# 1b
def create_connection(device_info):

   device_type = device_info.pop("device_type")
   driver = get_network_driver(device_type)
   device_conn_obj = driver(**device_info)

   return device_conn_obj

my_cisco3_device = create_connection(cisco3)

# 1c
my_device_conn_objects = []

my_device_conn_objects.append(my_cisco3_device)

my_arista1_device = create_connection(arista1)
my_device_conn_objects.append(my_arista1_device)


# 1d
# print(my_device_conn_objects)
for my_device_conn_object in my_device_conn_objects:
   print("Napalm connection object: ")
   print(my_device_conn_object)
   print()
   my_device_conn_object.open()
   print("Get facts: ")
   pprint(my_device_conn_object.get_facts())
   print()
   print("Napalm platform: ")
   print(my_device_conn_object.platform)
   print()
