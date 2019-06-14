#!/usr/bin/env python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device (
       api_format = "xml",
       host = "nxos1.lasthop.io",
       username = "pyclass",
       password = getpass(),
       transport = "https",
       port = 8443,
       verify = False )

output = device.show("show interface Ethernet1/1")

#print(etree.tostring(output).decode())

# ex 7a
interface_name = output.find(".//interface").text
interface_state = output.find(".//state").text
interface_mtu = output.find(".//eth_mtu").text

print("Interface: {}; State: {}; MTU: {}".format(interface_name, interface_state, interface_mtu))
print()

# ex 7b
cmds = [ "show system uptime", "show system resources" ]

cmds_output = device.show_list(cmds)
print(cmds_output)
for cmd_output in cmds_output:
   print(etree.tostring(cmd_output).decode())

# ex 7c
cfg_cmds = [ "interface loopback 34", "description lo_34", "interface loopback 78", "description lo_78" ]
cfg_cmds_output = device.config_list(cfg_cmds)
for cfg_cmd_output in cfg_cmds_output:
   print(etree.tostring(cfg_cmd_output).decode())



