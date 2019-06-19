#!/usr/bin/env python
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError

from pprint import pprint
from jnpr_devices import srx2


jnpr_device = Device(**srx2)
jnpr_device.open()
jnpr_device.timeout = 60

# 3a
jnpr_device_cfg = Config(jnpr_device)

jnpr_device_cfg.lock()

try:
   jnpr_device_cfg.lock()
except LockError as e:
   print("Config session already locked")

# 3b
print("Set new hostname in candidate config")
jnpr_device_cfg.load("set system host-name srx2-new-name", format = "set", merge = True)

# 3c
print("Check diff")
print(jnpr_device_cfg.diff())

# 3d
print("Rollback")
jnpr_device_cfg.rollback(0)

print("Check diff after rollback")
print(jnpr_device_cfg.diff())

print("Unlock config")
jnpr_device_cfg.unlock()


