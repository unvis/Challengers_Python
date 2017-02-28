#!/usr/bin/env python
# -*- coding: utf-8 -*-
access_template = ['switchport mode access','switchport access vlan %d','switchport nonegotiate','spanning-tree portfast','spanning-tree bpduguard enable']
print '\n'.join(access_template) % 5

print "абыр"