#!/usr/bin/env python
# -*- coding: utf-8 -*-

device=raw_input('enter device:\n')


#"{:<10} {:<10} {:<10} {:<10}".format(stringnet[0:8], stringnet[8:16], stringnet[16:24], stringnet[24:32])	

london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}


tuple_keys=tuple(london_co[device].keys())
string_keys=""
for i in london_co[device].keys():
	string_keys+=(i+",")
	
	
print string_keys



#print ("enter parameter name {:<30}:\n").format(tuple_keys)
#param=raw_input('enter parameter name {:<30}:\n').format(tuple_keys)

#print list_keys
#string_key=""
#print london_co[device][param]
#for k in london_co['r1']:
#	print k 

#temp = set(london_co)
#print temp