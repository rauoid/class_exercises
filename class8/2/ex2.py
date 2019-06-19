#!/usr/bin/env python
from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable

from pprint import pprint
from jnpr_devices import srx2

def check_connected(jnpr_device_obj):
   ''' check connection status to jnpr device obj '''
   connection_status = jnpr_device_obj.connected
   return connection_status

def gather_routes(jnpr_device_obj):
   ''' returns routing table for juniper device obj'''
   routing_table_obj = RouteTable(jnpr_device_obj)
   routing_table = routing_table_obj.get()
   return routing_table

def gather_arp_table(jnpr_device_obj):
   ''' returns arp table for juniper device obj '''
   arp_table_obj = ArpTable(jnpr_device_obj)
   arp_table = arp_table_obj.get()
   return arp_table

def print_output(jnpr_device_obj, jnpr_route_table, jnpr_arp_table):
   ''' prints jnpr route and arp tables for device obj '''

   print("Device hostname : {}".format(jnpr_device_obj.hostname))
   print("NETCONF port : {}".format(jnpr_device_obj.port))
   print("Username for connection : {}".format(jnpr_device_obj.user))
   print()

   print("Routing table:")
   for k, v in jnpr_route_table.items():
      print("Destination : {} , {}".format(k,v))
   print()

   print("Arp table:")
   for k, v in jnpr_arp_table.items():
      print("MAC address : {} , {}".format(k,v))
   print()

## check if running as main program ##
if __name__ == "__main__":

   jnpr_device = Device(**srx2)
   jnpr_device.open()

# 2a
   connection_status = check_connected(jnpr_device)
   print("Is the connection up to {} ? : {}".format(srx2['host'], connection_status))
   print()

# 2b
   routing_table = gather_routes(jnpr_device)
   arp_table = gather_arp_table(jnpr_device)

   print_output(jnpr_device, routing_table, arp_table)
