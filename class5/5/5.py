#!/usr/bin/env python
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

template_file="cisco3.j2"


template = env.get_template(template_file)

output = template.render()

print(output)

