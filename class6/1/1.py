#!/usr/bin/env python
import pyeapi
from getpass import getpass

connection = pyeapi.client.connect (
                      transport = "https",
                      host = "arista3.lasthop.io",
                      username = "pyclass",
                      password = getpass(),
                      port = "443" )

device = pyeapi.client.Node(connection)

output = device.enable("show ip arp")

ipv4neighbors = output[0]['result']['ipV4Neighbors']

for neighbor in ipv4neighbors:
 print("ip_address: {}, mac_address : {} ".format(neighbor['address'], neighbor['hwAddress']))

