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





