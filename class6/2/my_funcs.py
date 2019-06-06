#!/usr/bin/env python
from getpass import getpass
import yaml

def function1(conn_filename_yaml):
   arista4_conn = []
   arista4_yaml_file = conn_filename_yaml

   with open(arista4_yaml_file) as stream:
      arista4_conn = yaml.safe_load(stream)

   arista4_conn['password'] = getpass()
   return arista4_conn

def function2(output):
   ipv4neighbors = output[0]['result']['ipV4Neighbors']

   for neighbor in ipv4neighbors:
      print("ip_address: {}, mac_address : {} ".format(neighbor['address'], neighbor['hwAddress']))


