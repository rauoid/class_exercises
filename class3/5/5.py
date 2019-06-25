#!/usr/bin/env python
import yaml
from netmiko import ConnectHandler

devices_yaml="../../../.netmiko.yml"

with open(devices_yaml, 'r') as f:
    devices = yaml.load(f)

cisco3 = devices['cisco3']

nm = ConnectHandler(**cisco3)

cisco3_prompt=nm.find_prompt()

print(cisco3_prompt)

nm.disconnect()
