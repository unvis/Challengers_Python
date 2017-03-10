#!/usr/bin/env python
# -*- coding: utf-8 -*-
info=raw_input('enter information\n')
net=info.split("/")[0]
mask=info.split("/")[1]


print "Network:"
print "{:10} {:10} {:10} {:10} \n{:10} {:10} {:10} {:10}".format(net.split(".")[0], net.split(".")[1], net.split(".")[2], net.split(".")[3], bin(int(net.split(".")[0]))[2:].zfill(10), bin(int(net.split(".")[1]))[2:].zfill(10), bin(int(net.split(".")[2]))[2:].zfill(10), bin(int(net.split(".")[3]))[2:].zfill(10))


stroka=115
int(list(str(bin(stroka)))[3])
