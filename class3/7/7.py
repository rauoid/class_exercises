#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse


bgp_config = '''
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
'''

bgp_ngbrs_list = []

cp_obj = CiscoConfParse(bgp_config.splitlines())

rtr_bgp = cp_obj.find_objects(r"^\s+neighbor")

for ngb in rtr_bgp:
   ngb_ip = ngb.text.strip().split()[1]
   ngb_r_as = ngb.re_search_children(r"remote-as")
   ngb_r_as_nr = ngb_r_as[0].text.strip().split()[1]
   bgp_ngbrs_tpl = (ngb_ip, ngb_r_as_nr)
   bgp_ngbrs_list.append(bgp_ngbrs_tpl)

print("BGP Peers:")
print(bgp_ngbrs_list)   
