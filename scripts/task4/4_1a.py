#!/usr/bin/env python
# -*- coding: utf-8 -*-
info=raw_input('enter information\n')

#info="192.168.10.255/24"
net=info.split("/")[0]
mask=info.split("/")[1]



stringaddress=bin(int(net.split(".")[0]))[2:].zfill(8) + bin(int(net.split(".")[1]))[2:].zfill(8) + bin(int(net.split(".")[2]))[2:].zfill(8) + bin(int(net.split(".")[3]))[2:].zfill(8)
stringmask=""
stringnet=""

for i in range(0,32,1):
	if (i < int(mask)):
		stringmask+="1"
	else:
		stringmask+="0"
	stringnet+=str(int(stringaddress[i]) * int(stringmask[i]))
	
print net


print "Network:"
#print "{:10} {:10} {:10} {:10}".format(net.split(".")[0], net.split(".")[1], net.split(".")[2], net.split(".")[3])
#print "{:10} {:10} {:10} {:10}\n".format(bin(int(net.split(".")[0]))[2:].zfill(8), bin(int(net.split(".")[1]))[2:].zfill(8), bin(int(net.split(".")[2]))[2:].zfill(8), bin(int(net.split(".")[3]))[2:].zfill(8))
print "{:<10} {:<10} {:<10} {:<10}".format(int(stringnet[0:8],2), int(stringnet[8:16],2), int(stringnet[16:24],2), int(stringnet[24:32],2))
print "{:<10} {:<10} {:<10} {:<10}".format(stringnet[0:8], stringnet[8:16], stringnet[16:24], stringnet[24:32])	
print "Mask:"
print "/{}".format(mask)
print "{:<10} {:<10} {:<10} {:<10}".format(int(stringmask[0:8],2), int(stringmask[8:16],2), int(stringmask[16:24],2), int(stringmask[24:32],2))
print "{:<10} {:<10} {:<10} {:<10}".format(stringmask[0:8], stringmask[8:16], stringmask[16:24], stringmask[24:32])	


#print stringaddress
#print stringmask

#from subprocess import call
#call('ls')
#call('ls')
#https://docs.python.org/2/library/subprocess.html


#import os
#aaa=os.system('ping ya.ru -c 1')
#print aaa

#print stringnet

#a="111"
#print (str(int(stringnet[8:16],2)) + ".")

