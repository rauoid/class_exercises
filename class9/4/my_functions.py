#!/usr/bin/env python3
from napalm import get_network_driver

def open_napalm_connection(device_info):

   device_type = device_info.pop("device_type")
   driver = get_network_driver(device_type)
   device_conn_obj = driver(**device_info)

   return device_conn_obj

def create_backup(napalm_conn_obj):

# create backup file name from hostname
   bkp_filename = str(napalm_conn_obj.hostname)+".cfg_bkp"

   napalm_conn_obj.open()

   running_config = napalm_conn_obj.get_config("running")['running']

# remove "Building conf .." and "Current conf.." lines from IOS backup
   if napalm_conn_obj.platform == "ios":
#      print("ios detected")
      running_config_list = running_config.split("\n")
      running_config_cleaned_up = ""
      for line in running_config_list:
         if "Building configuration..." in line:
#            print("building")
            continue
         if "Current configuration :" in line:
#            print("current conf")
            continue
         if line == "" :
#            print("nothing")
            continue

         running_config_cleaned_up = running_config_cleaned_up + line + "\n"

      running_config = running_config_cleaned_up


# write config to file
   with open(bkp_filename, "w") as f:
      f.write(running_config)

# verify config backup
   napalm_conn_obj.load_replace_candidate(filename = bkp_filename)

   config_diff = napalm_conn_obj.compare_config()

   if config_diff is "":
      print("Backup successful")
   else:
      print("Backup failed !!!")

   napalm_conn_obj.discard_config()


def create_checkpoint(napalm_conn_obj):
   checkpoint_filename = "nxos.checkpoint"

   napalm_conn_obj.open()

   checkpoint = napalm_conn_obj._get_checkpoint_file()

   with open(checkpoint_filename, "w") as f:
      f.write(checkpoint)
