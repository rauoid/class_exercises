#!/usr/bin/env python3
from pprint import pprint
from my_devices import cisco3, arista1
from my_functions import open_napalm_connection, create_backup

arista1_lo_cfg_file = "arista1.lasthop.io-loopbacks"
cisco3_lo_cfg_file = "cisco3.lasthop.io-loopbacks"

my_devices_conn_cfg = []

cisco3_dict = {}
cisco3_dict['lo_cfg_file'] = cisco3_lo_cfg_file

arista1_dict = {}
arista1_dict['lo_cfg_file'] = arista1_lo_cfg_file

my_cisco3_device = open_napalm_connection(cisco3)
cisco3_dict['conn_obj'] = my_cisco3_device

my_devices_conn_cfg.append(cisco3_dict)

my_arista1_device = open_napalm_connection(arista1)
arista1_dict['conn_obj'] = my_arista1_device

my_devices_conn_cfg.append(arista1_dict)


for my_devices_conn_cfg_item in my_devices_conn_cfg:
# 3a
   print("Napalm connection object: {}".format(my_devices_conn_cfg_item['conn_obj']))
   print("Lo cfg file: {}".format(my_devices_conn_cfg_item['lo_cfg_file']))
   print()
   my_devices_conn_cfg_item['conn_obj'].open()
# 3b
   my_devices_conn_cfg_item['conn_obj'].load_merge_candidate(filename=my_devices_conn_cfg_item['lo_cfg_file'])
   print("Comparing config:")
   print(my_devices_conn_cfg_item['conn_obj'].compare_config())
   print()
# 3c
   print("Commiting config..")
   my_devices_conn_cfg_item['conn_obj'].commit_config()
   print("Comparing config:")
   print(my_devices_conn_cfg_item['conn_obj'].compare_config())
   print()

