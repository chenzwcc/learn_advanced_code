# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/10 下午2:42

"""
python自省  在运行时能够获得对象的类型。

    type()，判断对象类型
    dir()， 带参数时获得该对象的所有属性和方法；不带参数时，返回当前范围内的变量、方法和定义的类型列表
    isinstance()，判断对象是否是已知类型
    hasattr()，判断对象是否包含对应属性
    getattr()，获取对象属性
    setattr()， 设置对象属性

"""
# type
print(type(123))  # <class 'int'>
print(type('123'))  # <class 'str'>
print(type(None))  # <class 'NoneType'>

# dir
print(dir(123))  # dir(123) <==> dir(int),dir('123') <==> dir(str)
print(dir())

# isinstance
a = 123
b = '123'

print(isinstance(a, int))  # True
print(isinstance(b, str))  # True


# hasattr

class Obj(object):

    def __init__(self, x):
        self.x = x


obj = Obj(1)
print(hasattr(obj, 'x'))  # True
print(hasattr(obj, 'y'))  # False

# getattr
print(getattr(obj, 'x', 123))  # 1
print(getattr(obj, 'y', 123))  # 123

# setattr
setattr(obj, 'y', 123)
print(getattr(obj, 'y', None))  # 123
