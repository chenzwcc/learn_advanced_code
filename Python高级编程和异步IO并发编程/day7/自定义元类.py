# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/15 下午3:59

"""

"""

Student = type('Student',(object,),{'name':"chenzecc"})

stu1 = Student()
print(getattr(stu1,'name',None))


def __init__(self,name):
    self.name = name

def test(self):
    print('0000')

People = type('People',(object,),{"__init__":__init__,"test":test})
people = People("chenzw")
print(people.name)
people.test()


class Base(object):
    pass

class NewBase(Base):
    foo = True

Foo = type('Foo',(NewBase,),{'foo':False})

foo = Foo()
print(foo.foo)