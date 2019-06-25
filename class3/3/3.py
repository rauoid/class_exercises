#!/usr/bin/env python
import json

if_file="if.json"

with open(if_file, 'r') as f:
   if_info = json.load(f)

print(if_info.keys())
print()

ipv4_list=[]
ipv6_list=[]

for if_item in if_info:
   print(if_info[if_item].items())
   if "ipv4" in if_info[if_item].keys():
      for ipv4_value, ipv4_prefix in if_info[if_item]['ipv4'].items():
         ipv4=str(ipv4_value)+'/'+str(ipv4_prefix['prefix_length'])
         ipv4_list.append(ipv4)
   if "ipv6" in if_info[if_item].keys():
      for ipv6_value, ipv6_prefix in if_info[if_item]['ipv6'].items():
         ipv6=str(ipv6_value)+'/'+str(ipv6_prefix['prefix_length'])
         ipv6_list.append(ipv6)


print(ipv4_list)
print(ipv6_list)
