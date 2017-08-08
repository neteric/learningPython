#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 17/8/8 09:11
# Author  : Eric.Zhang
str1 = "                abcdef cccddd eeeeffff "
str2 = " abcdef cccddd" \
       "eeeeffff"
str3 = "abcdef cccddd eeeeffff"
# print str1.index(str2, 1, 20)
# print str1.find(str2, 1, 20)
## print str1.center(3, ",")
# print str1.count("c", 0, 4)
print str1.strip()
print str2.strip("\n")
print str3.strip("d  ")