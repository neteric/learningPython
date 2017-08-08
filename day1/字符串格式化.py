#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 17/8/7 20:04
# Author  : Eric.Zhang
name = raw_input("Name:")
age = int(raw_input("Age:"))
job = raw_input("Job:")
print ("the information of %s:\nName:%s\nAge:%s\nJob:%s\n" % (name, name, age, job))

print "the information of %s:\nName:%s\nAge:%s\nJob:%s\n" % (name, name, age, job)

print "the informat of:" + name + "\nName:" + name + "\nAge:" + age +"\nJob：" +job

msg = '''
The information of %s:
    name:%s
    age:%d
        job:%s
''' % (name, name, age, job)

print(msg)
