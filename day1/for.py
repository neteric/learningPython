#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 17/8/7 19:02
# Author  : Eric.Zhang
lucklyNumber = 3
for i in range(3):
    gustNumber = int(raw_input("please input your lucklyNumber:"))
    if gustNumber < lucklyNumber:
        print "to small"
    elif gustNumber > lucklyNumber:
        print "to large"
    else:
        print "Bingo!"
        break
else:
    print "to max retrys!"
