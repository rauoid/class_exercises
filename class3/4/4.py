#!/usr/bin/env python
import json

if_file="arista.json"

with open(if_file, 'r') as f:
   if_info = json.load(f)

# key ip address, value mac address in disct

my_dict = {}


for item in if_info['ipV4Neighbors']:
   my_dict[item['address']] = item['hwAddress']

print(my_dict)

