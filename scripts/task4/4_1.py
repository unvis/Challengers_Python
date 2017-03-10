#!/usr/bin/env python
# -*- coding: utf-8 -*-
#info=raw_input('enter information\n')
info="192.168.10.255/24"
net=info.split("/")[0]
mask=info.split("/")[1]


#print "Network:"
#print "{:10} {:10} {:10} {:10} \n{:10} {:10} {:10} {:10}".format(net.split(".")[0], net.split(".")[1], net.split(".")[2], net.split(".")[3], bin(int(net.split(".")[0]))[2:].zfill(10), bin(int(net.split(".")[1]))[2:].zfill(10), bin(int(net.split(".")[2]))[2:].zfill(10), bin(int(net.split(".")[3]))[2:].zfill(10))



# Вывести число
#stroka=115
#int(list(str(bin(stroka)))[3])


# bin(int(net.split(".")[0]))[2:].zfill(10)

stringaddress=bin(int(net.split(".")[0]))[2:].zfill(8) + bin(int(net.split(".")[1]))[2:].zfill(8) + bin(int(net.split(".")[2]))[2:].zfill(8) + bin(int(net.split(".")[3]))[2:].zfill(8)
stringmask=""
stringnet=""

for i in range(0,32,1):
    if (i < int(mask)):
	stringmask+="1"
    else:
	stringmask+="0"
print stringaddress
print stringmask

for i in range(0,32,1):
	stringnet+=str(int(stringaddress[i]) * int(stringmask[i]))


print stringnet
