#!/usr/bin/env python
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

template_file="vrf_config.j2"

vrf_config = { "vrf_name" : "blue",
               "rd_number" : "100:1",
               "ipv4_enabled" : True,
               "ipv6_enabled" : False,
              }

template = env.get_template(template_file)

output = template.render(**vrf_config)

print(output)

