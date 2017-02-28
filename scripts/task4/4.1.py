#!/usr/bin/env python
# -*- coding: utf-8 -*-
info=raw_input('enter information\n')

print "Network:"
print "{:10} {:10} {:10} {:10} \n{:10} {:10} {:10} {:10}".format(info.split(".")[0], info.split(".")[1], info.split(".")[2], info.split(".")[3], bin(int(info.split(".")[0]))[2:].zfill(10), bin(int(info.split(".")[1]))[2:].zfill(10), bin(int(info.split(".")[2]))[2:].zfill(10), bin(int(info.split(".")[3]))[2:].zfill(10))

