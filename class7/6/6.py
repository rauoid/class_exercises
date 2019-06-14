#!/usr/bin/env python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from pprint import pprint

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device (
       api_format = "jsonrpc",
       host = "nxos1.lasthop.io",
       username = "pyclass",
       password = getpass(),
       transport = "https",
       port = 8443,
       verify = False )

output = device.show("show interface Ethernet1/1")

print("Interface: {}; State: {}; MTU: {}".format(output['TABLE_interface']['ROW_interface']['interface'], 
                                                 output['TABLE_interface']['ROW_interface']['state'],
                                                  output['TABLE_interface']['ROW_interface']['eth_mtu'] ))

