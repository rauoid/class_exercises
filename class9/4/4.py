#!/usr/bin/env python3
from pprint import pprint
from my_devices import cisco3, arista1, nxos1
from my_functions import open_napalm_connection, create_backup, create_checkpoint
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#my_device_conn_objects = []
#
#my_cisco3_device = open_napalm_connection(cisco3)
#my_device_conn_objects.append(my_cisco3_device)
#
#my_arista1_device = open_napalm_connection(arista1)
#my_device_conn_objects.append(my_arista1_device)

my_nxos1_device = open_napalm_connection(nxos1)

print(my_nxos1_device)
# 4b
create_checkpoint(my_nxos1_device)

# 4c, file nxos1.config, added "int lo130"
## interface loopback130
##   description loopback130
##   !#no shutdown
nxos1_config_file = "nxos1.full_config"

# 4d
my_nxos1_device.open()
my_nxos1_device.load_replace_candidate(filename = nxos1_config_file)

print("Compare config:")
print(my_nxos1_device.compare_config())

print("Discarding candidate config:")
my_nxos1_device.discard_config()

print("Compare config:")
print(my_nxos1_device.compare_config())

