# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/9 下午10:38

"""
属性查找方式：先查找实例变量是否存在，没有就去类变量查找，再没有就报错

"""


class A(object):
    z = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(1, 2)

print(a.x, a.y, a.z, A.z)
print(a.z is A.z)

a.z = 100  # 相当于重新给a实例添加了一个z属性 
print(a.z, A.z)


