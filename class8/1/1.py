#!/usr/bin/env python
from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

jnpr_device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())

jnpr_device.open()

jnpr_device_facts = jnpr_device.facts
pprint(jnpr_device_facts)

print()

hostname_fact = jnpr_device_facts
print(hostname_fact['hostname'])
