#!/usr/bin/env python
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
from my_devices import nxos1, nxos2
import time

nxos_devices = [ nxos1, nxos2 ]

nxos1_cfg_file = "nxos1_cfg_file.txt"
nxos2_cfg_file = "nxos2_cfg_file.txt"

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

template_file="nxos_cfg_template.j2"

nxos1_cfg = { "interface" : "Ethernet1/1",
          "ip_address" : "10.1.100.1",
          "netmask" : "24",
          "local_as" : "22",
          "peer_ip_address" : "10.1.100.2"}

nxos2_cfg = { "interface" : "Ethernet1/1",
          "ip_address" : "10.1.100.2",
          "netmask" : "24",
          "local_as" : "22",
          "peer_ip_address" : "10.1.100.1"}

nxos_devices_cfg = [ nxos1_cfg, nxos2_cfg ]

template = env.get_template(template_file)

####
print("Writing config to file")

# nxos1
output = template.render(**nxos1_cfg)
print(output)
with open(nxos1_cfg_file, "w") as f:
   f.write(output)

# nxos2
output = template.render(**nxos2_cfg)
print(output)
with open(nxos2_cfg_file, "w") as f:
   f.write(output)

####
print("Sending config to devices")
# nxos1
nm = ConnectHandler(**nxos1)
cmd_output = nm.send_config_from_file(config_file=nxos1_cfg_file)
print(cmd_output)
nm.disconnect()

#nxos2
nm = ConnectHandler(**nxos2)
cmd_output = nm.send_config_from_file(config_file=nxos2_cfg_file)
print(cmd_output)
nm.disconnect()

####
print("Verify device config")

print("Sleeping 5 sec")
time.sleep(5)

# nxos1
nm = ConnectHandler(**nxos1)
cmd_output = nm.send_command("ping 10.1.100.2 count 3")
print(cmd_output)
cmd_output = nm.send_command("show ip bgp neighbors")
print(cmd_output)
nm.disconnect()

# nxos2
nm = ConnectHandler(**nxos2)
cmd_output = nm.send_command("ping 10.1.100.1 count 3")
print(cmd_output)
cmd_output = nm.send_command("show ip bgp neighbors")
print(cmd_output)
nm.disconnect()








