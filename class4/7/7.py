#!/usr/bin/env python
import textfsm
from pprint import pprint

template_file="show_interfaces_status.template"

template = open(template_file)

with open("show_interfaces_status.txt") as f:
   raw_text_data = f.read()

re_table = textfsm.TextFSM(template)

data = re_table.ParseText(raw_text_data)

my_list = []
my_dict = {}

for item in data:
   my_dict['PORT_NAME'] = item[0]
   my_dict['STATUS'] = item[1]
   my_dict['VLAN'] = item[2]
   my_dict['DUPLEX'] = item[3]
   my_dict['SPEED'] = item[4]
   my_dict['PORT_TYPE'] = item[5]
   my_list.append(my_dict)

pprint(my_list)
   
