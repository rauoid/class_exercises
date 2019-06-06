#!/usr/bin/env python
import pyeapi
from getpass import getpass
import yaml

arista4_yaml_file = "arista4.yaml"

with open(arista4_yaml_file) as stream:
   arista4_conn = yaml.safe_load(stream)

arista4_conn['password'] = getpass()

connection = pyeapi.client.connect (**arista4_conn)

device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

ipv4neighbors = output[0]['result']['ipV4Neighbors']

for neighbor in ipv4neighbors:
 print("ip_address: {}, mac_address : {} ".format(neighbor['address'], neighbor['hwAddress']))


