# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/5/10 下午3:28

"""
type -> class -> object: object通过class实例化得到，class通过实例化type得到
object 是最顶层的基类，包括type也是继承object得到


在python中为什么说一切皆对象？
    简单点说就是 type继承object，object实例后类型又是type类型，而type通过实例又能得到type,形成了闭环。
    可以通过type创建任意对象，包括type自身
"""


class CustomClass:
    def __init__(self):
        pass


my_class = CustomClass
print(type(my_class()))
print(type(my_class))

print(my_class.__bases__)
print(type.__bases__)
print(object.__bases__)

print(type(type))

print(type(object))

