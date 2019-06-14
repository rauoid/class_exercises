#!/usr/bin/env python
import xmltodict

xmlfile1 = "show_security_zones_trust.xml"
xmlfile2 = "show_security_zones.xml"

def parsexmltodict(xml_file):
   with open(xml_file) as f:
     xml_data = f.read().strip()

   my_xml = xmltodict.parse(xml_data)
   return my_xml

def parsexmltodict_forcelist(xml_file, xml_element_name ):
   with open(xml_file) as f:
     xml_data = f.read().strip()

   my_xml = xmltodict.parse(xml_data, force_list = { xml_element_name : True})
   return my_xml



# ex 3a
xmlfile1_dict = parsexmltodict(xmlfile1)
xmlfile2_dict = parsexmltodict(xmlfile2)
print()

# ex 3b
print(type(xmlfile1_dict['zones-information']['zones-security']))
print(type(xmlfile2_dict['zones-information']['zones-security']))
print()

# ex 3c
xmlfile1_dict_forcelist = parsexmltodict_forcelist(xmlfile1, "zones-security")
print(type(xmlfile1_dict_forcelist['zones-information']['zones-security']))

