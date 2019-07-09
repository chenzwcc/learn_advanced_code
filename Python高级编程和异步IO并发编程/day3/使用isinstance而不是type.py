# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/9 下午10:30


"""
项目中判定一个对象是否为某个类的实例，用isinstance而不是type，
因为使用type不会考虑到继承的问题

"""


class A(object):
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B))
print(isinstance(b, A))

print(type(b) is B)
print(type(b) is A)
