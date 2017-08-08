#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 17/8/8 19:04
# Author  : Eric.Zhang

f = open("test.txt", "w+")
f.write("This is the first line\n")
f.write("This is the second line\n")
f.write("This is the 3 line\n")
f.write("This is the 4 line\n")
f.close()

f = open("test.txt","r")
# print f.readlines()
for line in f:
    print line,
f.close()

f = open("test.txt", "a+")
f.write("5\n")
f.write("6\n")
f.write("7")
f.write("8")

f.close()

f = open("test.txt","r")
# print f.readlines()
for line in f:
    print line,
f.close()