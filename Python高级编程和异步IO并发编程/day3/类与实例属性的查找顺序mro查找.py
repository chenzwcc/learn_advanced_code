# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/10 上午10:06

"""
MRO:methods resolution order

"""


class A(object):

    def say(self):
        print("this is a class")


class B(A):

    def say(self):
        print("this is b class")


class C(A):
    def say(self):
        print("this is c class")


class D(C, B):
    pass


d = D()
print(d.say())  # this is c class
print(
    D.__mro__)  # (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


class AA(object):
    pass


class BB(object):
    pass


class CC(AA):
    pass


class DD(BB):
    pass


class EE(CC, DD):
    pass


print(
    EE.__mro__)  # (<class '__main__.EE'>, <class '__main__.CC'>, <class '__main__.AA'>, <class '__main__.DD'>, <class '__main__.BB'>, <class 'object'>)
