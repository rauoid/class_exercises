#!/usr/bin/env python
import pyeapi
from getpass import getpass
import yaml
import my_funcs


arista4_yaml_file = "arista4.yaml"

# read arista4 connection params from yaml config file
arista4_conn = my_funcs.function1(arista4_yaml_file)

connection = pyeapi.client.connect (**arista4_conn)
device = pyeapi.client.Node(connection)

output = device.enable("show ip route")

# print output 
my_funcs.function2(output)

