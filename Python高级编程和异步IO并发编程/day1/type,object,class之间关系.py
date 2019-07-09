# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/5/10 下午3:28

"""
type -> class -> object: object通过class实例化得到，class通过实例化type得到
object 是最顶层的基类，包括type也是继承object得到
object 顶层基类为空


在python中为什么说一切皆对象？
    简单点说就是 type继承object，object又是通过type实例化得到的，而type通过实例又能得到type,形成了闭环。
    可以通过type创建任意对象，包括type自身。


    一句话概括就是：在python中所有的实例对象追究本源都是通过type实例化得到的(type->class->object)，并且type实例对象也是
                  通过type实例化得到的，所以说python一切皆对象。
"""

a = 1
b = '123'
print(type(a))
print(type(int))
# type -> int -> 1


class CustomClass:
    def __init__(self):
        pass


my_class = CustomClass
print(type(my_class()))

# 打印my_class的基类
print(my_class.__bases__)
print(type.__bases__)
print(object.__bases__)

print(type(type))

print(type(object))


class A(object):
    pass


class B(A):
    pass


print(B.__bases__)
