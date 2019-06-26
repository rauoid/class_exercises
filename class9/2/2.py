#!/usr/bin/env python3
# from napalm import get_network_driver
from pprint import pprint
from my_devices import cisco3, arista1
from my_functions import open_napalm_connection


my_device_conn_objects = []

my_cisco3_device = open_napalm_connection(cisco3)
my_device_conn_objects.append(my_cisco3_device)

my_arista1_device = open_napalm_connection(arista1)
my_device_conn_objects.append(my_arista1_device)


# print(my_device_conn_objects)
for my_device_conn_object in my_device_conn_objects:
   print("Napalm connection object: ")
   print(my_device_conn_object)
   print()
# open connection
   my_device_conn_object.open()
# 2b get arp table
   print("Get arp table: ")
   pprint(my_device_conn_object.get_arp_table())
   print()
#
#   print("Napalm platform: ")
#   print(my_device_conn_object.platform)
#   print()
