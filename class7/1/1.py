#!/usr/bin/env python
from lxml import etree

xml_file = "show_security_zones.xml"

#my_xml = etree.parse(xml_file)

with open(xml_file) as f:
  xml_data = f.read().strip()

my_xml = etree.fromstring(xml_data)

# ex 1a
print(my_xml)
print(type(my_xml))
print()

# ex 1b
print()
print(etree.tostring(my_xml).decode())
print()

# ex 1c
print(my_xml.tag)
print(len(my_xml.getchildren()))
print()

# ex 1d
print(my_xml[0].tag)
print(my_xml.getchildren()[0].tag)
print()

# ex 1e
trust_zone = my_xml.getchildren()[0]
print(trust_zone[0].text)
print()

# ex 1f
for child in trust_zone:
   print(child.tag)
