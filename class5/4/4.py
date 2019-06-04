#!/usr/bin/env python
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

template_file="vrf_config.j2"


vrf_config_list = [ 
             { "vrf_name" : "blue", "rd_number" : "100:1", "ipv4_enabled" : True, "ipv6_enabled" : False }, 
             { "vrf_name" : "green", "rd_number" : "101:1", "ipv4_enabled" : False, "ipv6_enabled" : True}, 
             { "vrf_name" : "yellow", "rd_number" : "102:1", "ipv4_enabled" : True, "ipv6_enabled" : True},
             { "vrf_name" : "black", "rd_number" : "103:1", "ipv4_enabled" : True, "ipv6_enabled" : False},
             { "vrf_name" : "white", "rd_number" : "104:1", "ipv4_enabled" : True, "ipv6_enabled" : False},
             ]


vrf_config = { "vrf_config_list" : vrf_config_list }

template = env.get_template(template_file)

output = template.render(**vrf_config)

print(output)

