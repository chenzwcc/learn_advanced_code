# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/16 下午3:45

"""
判定一个对象是否是可迭代对象就要看他内部是否实现__iter__方法。
判定一个对象是否是迭代器对象就要看他内部是否实现__iter__,__next__方法。
"""
from collections.abc import Iterable, Iterator

list1 = [1,2]

print(isinstance(list1,Iterable))  # True
print(isinstance(list1,Iterator))  # False

iter_ator = iter(list1)
print(isinstance(iter_ator,Iterator))  # True


class Peo(object):
    def __init__(self):
        pass

    def __iter__(self):
        pass

    # def __next__(self):
    #     pass

peo = Peo()
print(isinstance(peo,Iterable))  # True
print(isinstance(peo,Iterator))  # False