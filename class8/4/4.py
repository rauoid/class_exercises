#!/usr/bin/env python
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError
import sys

from pprint import pprint
from jnpr_devices import srx2
from ex2 import gather_routes

routes_cfg_file = "jnpr_routes.cfg"

jnpr_device = Device(**srx2)
jnpr_device.open()
jnpr_device.timeout = 60

 
jnpr_device_cfg = Config(jnpr_device)

try:
   jnpr_device_cfg.lock()
except LockError as e:
   print("Config session already locked, exiting")
   sys.exit()

# get current routing table
routing_table = gather_routes(jnpr_device)

# install routing from file
jnpr_device_cfg.load(path = routes_cfg_file, format = "text", merge = True)

# commit change
jnpr_device_cfg.commit(comment="adding 2 discard routes")

# get routing table after config change
routing_table_new = gather_routes(jnpr_device)

# comparing routing tables
old_routes = []
new_routes = []
## build a list of dst routes for old table
for route in routing_table.items():
   old_routes.append(route[0])

for new_route in routing_table_new.items():
   if new_route[0] not in old_routes:
      new_routes.append(new_route)

print("New routes added : ")
print(new_routes)
print()

# remove routes
print("Removing routes")
jnpr_device_cfg.load("delete routing-options static route 203.0.113.50/32", format = "set", merge = True)
jnpr_device_cfg.load("delete routing-options static route 203.0.113.60/32", format = "set", merge = True)

print(jnpr_device_cfg.diff())
jnpr_device_cfg.commit(comment="deleting 2 discard routes")

# unlock config
jnpr_device_cfg.unlock()

