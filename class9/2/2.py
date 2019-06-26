#!/usr/bin/env python3
from pprint import pprint
from my_devices import cisco3, arista1
from my_functions import open_napalm_connection, create_backup


my_device_conn_objects = []

my_cisco3_device = open_napalm_connection(cisco3)
my_device_conn_objects.append(my_cisco3_device)

my_arista1_device = open_napalm_connection(arista1)
my_device_conn_objects.append(my_arista1_device)

for my_device_conn_object in my_device_conn_objects:
# 2a
   print("Napalm connection object: ")
   print(my_device_conn_object)
   print()
   my_device_conn_object.open()
# 2b get arp table
   print("Get arp table: ")
   pprint(my_device_conn_object.get_arp_table())
   print()
# 2c get ntp peers
   print("Get NTP peers: ")
   try:
      print("NTP peers: {}".format(my_device_conn_object.get_ntp_peers()))
   except NotImplementedError:
      print("Command not implemented")
      print()
# 2d create backup
   create_backup(my_device_conn_object)
   print()
