#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 17/8/9 16:20
# Author  : Eric.Zhang
import os
dataDiskID = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
journalDisk = ['k', 'l']
a = []
b = []
c = []
for hostID in range(01, 05):
    for disk in dataDiskID:
        disk = "/dev/sd" + disk
        a.append("compute" + str(hostID) + ":" + disk)

for disk in journalDisk:
    for diskID in range(1, 6):
        b.append("/dev/sd" + disk + str(diskID))

for x, y in enumerate(a,):
    c.append(y + ":" + b[x % 10])

for i in c:
    os.system("ceph-deploy osd prepare c[i]")
    os.system("ceph-deploy osd prepare c[i]")
