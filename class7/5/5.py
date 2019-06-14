#!/usr/bin/env python
from lxml import etree

xmlfile = "show_version.xml"

with open(xmlfile, "rb") as f:
   xml_data = f.read().strip()

my_xml = etree.fromstring(xml_data)

# 5a
print(my_xml.nsmap)
print()

# 5b
print(my_xml.find(".//{*}proc_board_id").text)
