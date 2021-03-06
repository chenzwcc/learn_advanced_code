# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/10 下午3:48

"""
super执行顺序：可以调用类的__mro__获取
"""


class A(object):
    def go(self):
        print("go A go!")

    def stop(self):
        print("stop A stop!")

    def pause(self):
        raise Exception("Not Implemented")


class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")


class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")

    def stop(self):
        super(C, self).stop()
        print("stop C stop!")


class D(B, C):
    def go(self):
        super(D, self).go()
        print("go D go!")

    def stop(self):
        super(D, self).stop()
        print("stop D stop!")

    def pause(self):
        print("wait D wait!")


class E(B, C):
    pass


a = A()
b = B()
c = C()
d = D()
e = E()
print(D.__mro__)
# 说明下列代码的输出结果
# a.go()  # go a go
# print('--------')
# b.go()  # go a go go b go
# print('--------')
# c.go()  # go a go go c go
# print('--------')
# d.go()
# print('--------')
# e.go()
# print('--------')
# a.stop() # a stop
# print('--------')
# b.stop() # a stop
# print('--------')
# c.stop() # a stop c stop
# print('--------')
# d.stop() # a c d
# print('--------')
# e.stop() # a c
print(D.mro())
# a.pause() # Not Implemented
# b.pause() #Not Implemented
# c.pause() #Not Implemented
# d.pause() #wait D wait!
# e.pause() #Not Implemented
