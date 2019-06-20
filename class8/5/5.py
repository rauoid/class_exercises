#!/usr/bin/env python
from jnpr.junos import Device
from lxml import etree
from pprint import pprint
from jnpr_devices import srx2

jnpr_device = Device(**srx2)
jnpr_device.open()
jnpr_device.timeout = 60

# 5a
xml_out = jnpr_device.rpc.get_software_information()
print(etree.tostring(xml_out, encoding="unicode"))

# 5b
# show interfaces terse
xml_out = jnpr_device.rpc.get_interface_information()
print(etree.tostring(xml_out, encoding="unicode"))

# 5c
xml_out = jnpr_device.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))


