#!/usr/bin/env python
import xmltodict

xml_file = "show_security_zones.xml"

with open(xml_file) as f:
  xml_data = f.read().strip()

my_xml = xmltodict.parse(xml_data)

# ex 2a
print(my_xml)
print(type(my_xml))
print()

# ex 2b
for index, zones_security_item in enumerate(my_xml['zones-information']['zones-security'], 1):
   print("Security Zone #{}: {}".format(index, zones_security_item['zones-security-zonename']))
