#!/usr/bin/env python
import yaml

lab_devices = [ 
         {'hostname':'cisco3.lasthop.io', 'snmp_port':'161', 'ssh_port':'22', 'username':'user', 'password':'guessm3'},
         {"hostname":"cisco4.lasthop.io", "snmp_port":"161", "ssh_port":"22", "username":"user", "password":"guessm3"},
         {"hostname":"nxos1.lasthop.io", "snmp_port":"161", "ssh_port":"22", "username":"user", "password":"guessm3"},
         {"hostname":"nxos2.lasthop.io", "snmp_port":"161", "ssh_port":"22", "username":"user", "password":"guessm3"}
              ]
           


with open('2.yaml', 'wt') as f:
   yaml.dump(lab_devices, f, default_flow_style=False)
