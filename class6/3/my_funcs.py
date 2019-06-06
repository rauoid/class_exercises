#!/usr/bin/env python
from getpass import getpass
import yaml
from pprint import pprint

def function1(conn_filename_yaml):
   arista4_conn = []
   arista4_yaml_file = conn_filename_yaml

   with open(arista4_yaml_file) as stream:
      arista4_conn = yaml.safe_load(stream)

   arista4_conn['password'] = getpass()
   return arista4_conn

def function2(output):

   routes_vrf_default = output[0]['result']['vrfs']['default']['routes']

   for route in routes_vrf_default:
      print("Route : {}".format(route))
      route_type = (output[0]['result']['vrfs']['default']['routes'][route]['routeType'])
      print("Route type : {}".format(route_type))
      if route_type == "static":
         next_hop_addr = output[0]['result']['vrfs']['default']['routes'][route]['vias'][0]['nexthopAddr']
         print("Next hop address : {}".format(next_hop_addr))
      print()

