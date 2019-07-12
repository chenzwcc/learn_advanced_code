# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/11 下午4:37

"""
列表切片会返回一个新的列表
实现__getitem__即可完成切片功能
"""

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list1[::])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(id(list1), id(list1[::]))  # 会返回一个新的列表，所以ID不等

"""
Python的魔法方法__getitem__ 可以让对象实现迭代功能。
"""

class Company(object):

    def __init__(self,company_list):
        self.company_list = company_list

    def __getitem__(self, item):
        return self.company_list[item]


comapny = Company(['cp1','cp2','cp3','cp4'])
print(comapny[:9])