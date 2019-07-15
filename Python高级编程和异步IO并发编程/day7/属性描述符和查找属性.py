# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/15 下午1:22

"""
实现了__get__、__set__、__delete__ 方法的类是描述符，只要实现了其中一个就是。只不过只实现 __get__() 的话称为非数据描述符，意味着只可读，
同时实现 __get__(), 和 __set__() 称为数据描述符，意味着可读写。

描述符类：实现了描述符协议的类，即下面的InterField类。
托管类：将描述符类的实例作为类属性的类，即下面的NewPeople类。
托管实例：托管类的实例，即下面NewPeople类的实例newpeople的age类属性。
托管属性：托管类中由描述符实例处理的公开属性，例如NewPeople类的age类属性。
存储属性：可以粗略的理解为、托管实例的属性。
托管属性是类(NewPeople)属性、存储属性是实例(newpeople)的属性。
"""


class People(object):
    def __init__(self, name):
        self.name = name
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self, value):
        if value < 0:
            raise ValueError('负数不被允许输入')
        self._age = value

    @age.getter
    def get_age(self):
        return self._age


# 对于以上情况只是age,sex需要限制，如果有更多属性的话这样写代码量就太复杂了。所以出现了描述符。对于上面代码可以重构，如下：
class InterField(object):
    def __init__(self, attrname):
        self.attrname = attrname

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('负数不被允许输入')
        instance.__dict__[self.attrname] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.attrname]


class NewPeople(object):
    age = InterField("age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    people = People("chenzwcc")
    people.set_age = 10
    print(people.get_age)

    newpeople = NewPeople("chenzw", -1)
    print(newpeople.age)
    # Django中ORM的原理就是利用属性描述符
