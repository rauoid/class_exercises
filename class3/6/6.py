#!/usr/bin/env python
import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

devices_yaml="../../../.netmiko.yml"

with open(devices_yaml, 'r') as stream:
    devices = yaml.safe_load(stream)

cisco4 = devices['cisco4']

nm = ConnectHandler(**cisco4)


cisco4_config=nm.send_command("show run")
# print(cisco4_config)

cisco4_obj = CiscoConfParse(cisco4_config.splitlines())

interfaces_w_ip = cisco4_obj.find_objects_w_child(parentspec=r"interface", childspec=r"^\s+ip address")

# print(interfaces_w_ip)
print()

for interface in interfaces_w_ip:
   print("Interface Line: %s"  % (interface.text))
   ip_addr_list = interface.re_search_children(r"ip address")
#   print(ip_addr)
   for ip_addr in ip_addr_list:
      print("IP Address Line: %s" % (ip_addr.text))

nm.disconnect()
