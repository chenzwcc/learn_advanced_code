# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/12 上午10:39

"""
以升序的形式维护已排列的可变序列
"""

import bisect

list1 = []

bisect.insort(list1, 2)
bisect.insort(list1, 1)
bisect.insort(list1, 8)
bisect.insort(list1, 5)

print(list1)

print(bisect.bisect_right(list1, 2)) #
print(list1)
print(bisect.bisect_left(list1, 2))
print(list1)
 