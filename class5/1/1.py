#!/usr/bin/env python
from jinja2 import Template


bgp_vars = { "local_as":"10",
        "peer1_ip":"10.1.20.2",
        "peer1_as":"20",
        "peer2_ip":"10.1.30.2",
        "peer2_as":"30" }

# local_as, peer1_ip, peer1_as, peer2_ip, peer2_as. 

bgp_template='''router bgp {{ local_as }}
  neighbor {{ peer1_ip  }} remote-as {{ peer1_as }}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{ peer2_ip  }} remote-as {{ peer2_as }}
    address-family ipv4 unicast'''

j_obj = Template(bgp_template)

print(j_obj.render(**bgp_vars))



