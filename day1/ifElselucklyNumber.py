#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 17/8/3 23:16
# Author  : Eric.Zhang
for i in range(1, 3):
    print i
    lucklyNumber = 4
    inputNumber = int(raw_input("please a luckly number:"))
    if inputNumber < lucklyNumber:
        print "太小"
    elif inputNumber > lucklyNumber:
        print "太大"
    elif inputNumber == lucklyNumber:
        print ("bingo")
        exit(0)
    else:
        print "Error Input!!"
