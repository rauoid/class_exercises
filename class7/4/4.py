#!/usr/bin/env python
from lxml import etree

xmlfile = "show_security_zones.xml"

my_xml = etree.parse(xmlfile)
my_xml = my_xml.getroot()


# ex 4a
print()
print("Find tag of the first zones-security element")
print("--------------------")
zones_security_first = my_xml.find("zones-security")
print(zones_security_first.tag)
print()

print("Find tag of all child elements of the first zones-security element")
print("--------------------")
for child in zones_security_first.getchildren():
   print(child.tag)

print()
# ex 4b
print(my_xml.find(".//zones-security-zonename").text)
print()

# ex 4c
zones_security_all = my_xml.findall(".//zones-security")
for zones_security_item in zones_security_all:
   print(zones_security_item[0].text)


