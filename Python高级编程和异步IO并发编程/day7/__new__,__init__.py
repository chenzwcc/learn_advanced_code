# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/15 下午2:20

"""
new的功能是在生成对象之前所做的动作，接受的参数是cls 类
init是在对象生成之后完善对象的属性 它接受的是self 对象
对象生成是在 new 里面 return （返回一个对象）
"""


class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super(Person, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print(self, id(self))
        print('__init__')


if __name__ == "__main__":
    p1 = Person()
    print(id(p1))

# __new__
# <__main__.Person object at 0x00000000009E2B38> 10365752
# __init__
# 10365752

# 通过运行这段代码，可以看到，new方法的调用是发生在init之前的。其实当 实例化一个类的时候，具体的执行逻辑是这样的：
# p1 = Person()
# 首先执行使用name和age参数来执行Person类的new方法，这个new方法会
# 返回Person类的一个实例（通常情况下是使用
# super(Persion, cls).new(cls, … …) 这样的方式），
#
# 然后利用这个实例来调用类的init方法，上一步里面new产生的实例也就是init里面的的self（根据id(self)和id(p1)相等得知）
# 所以，init 和 new 最主要的区别在于：
# init通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。
# new通常用于控制生成一个新实例的过程。它是类级别的方法。
# new至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
# new必须要有返回值，返回实例化出来的实例，这点在自己实现new时要特别注意，可以return父类new出来的实例，或者直接是object的new出来的实例
# 可以将类比作制造商，new方法就是前期的原材料购买环节，init方法就是在有原材料的基础上，加工，初始化商品环节