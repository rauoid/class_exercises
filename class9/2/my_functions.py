#!/usr/bin/env python3
from napalm import get_network_driver

def open_napalm_connection(device_info):

   device_type = device_info.pop("device_type")
   driver = get_network_driver(device_type)
   device_conn_obj = driver(**device_info)

   return device_conn_obj
