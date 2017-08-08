#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 17/8/8 14:21
# Author  : Eric.Zhang
name_list = ['zhangchao', 'Beber', 'Chunp']

# 查询列表的所有方法
print help(name_list)
print dir(name_list)

# 列表追加（在列表尾追加）
name_list.append("Eric")

# 统计列表中摸个元素的个数
name_list.count("zhangsan")

#?
name_list.extend()

# 得到元素的索引
print name_list.index("Beber")

# 在列表的索引1处插入元素"lisi"
name_list.insert(1,"lisi")

# 按值删除元素
name_list.remove("Beber")

# 按索引删除元素，默认删除最后一个
name_list.pop(2)

# 删除列表中所有的"Beber"
for i in range(name_list.count("Beber")):
    BeberIndex = name_list.index("Beber")
    name_list.pop(BeberIndex)
#或者
for i in range(name_list.count("Beber")):
    name_list.remove("Beber")

# 反转列表
name_list.reverse()

# 列表排序
name_list.sort()

# 列表切片(列表切片顾前不顾后)
name_list2 = name_list[1:3]
name_list2 = name_list[0:]
name_list2 = name_list[:-1]  # 0-倒数第二个
name_list2 = name_list[0:4:2]  # 切片的步长为2

print name_list
