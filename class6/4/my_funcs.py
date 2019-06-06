#!/usr/bin/env python
import yaml

def function1(conn_filename_yaml):
   arista_conn = []
   arista_yaml_file = conn_filename_yaml

   with open(arista_yaml_file) as stream:
      arista_conn = yaml.safe_load(stream)

   return arista_conn
