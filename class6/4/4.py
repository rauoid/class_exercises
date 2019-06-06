#!/usr/bin/env python
import pyeapi
from getpass import getpass
import yaml
import my_funcs
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment 
from pprint import pprint

arista_yaml_file = "arista.yaml"

## jinja
loopback_j2_file = "loopback.j2"
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')
template = env.get_template(loopback_j2_file)

## one password for all devices
arista_password = getpass()

## get arista settings from yaml file
arista_devs = my_funcs.function1(arista_yaml_file)

for device_name in  arista_devs:
   print(device_name)

## settings for current device   
   arista_conf = arista_devs[device_name]

## set password
   arista_conf['password'] = arista_password

## create loopback dict
   arista_loopback = arista_conf['loopback']
   print(arista_loopback)

## remove loopback part from dict
   arista_conn = arista_conf
   del arista_conn['loopback']

## generate config
   loopback_config = template.render(**arista_loopback)
   print(loopback_config)
   loopback_config_dict = loopback_config.split("\n")
   print (loopback_config_dict)
## connect to arista
   connection = pyeapi.client.connect (**arista_conn)
   device = pyeapi.client.Node(connection)
## configure interfaces
   cfg_output = device.config(loopback_config_dict)
   print(cfg_output)
## verify interfaces
   output = device.enable("show ip interface brief")
   pprint(output)
   print()

