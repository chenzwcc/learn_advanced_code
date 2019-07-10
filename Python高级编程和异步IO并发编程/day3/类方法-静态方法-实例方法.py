# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/10 上午11:07

"""
实例方法

    定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；

    调用：只能由实例对象调用。

类方法

    定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；

    调用：实例对象和类对象都可以调用。

静态方法

    定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；

    调用：实例对象和类对象都可以调用。

"""


class Emplayee(object):

    def get_name(self):
        print("this is object method")

    @staticmethod
    def get_age():
        print("this is staticmethod")

    @classmethod
    def get_sex(cls):
        print("this is classmethod")


if __name__ == '__main__':
    emplayee = Emplayee()

    # 实例方法只能通过实例调用
    emplayee.get_name()

    # 静态方法可以通过类本身或者实例本身调用
    emplayee.get_age()
    Emplayee.get_age()

    # 类方法可以通过类本身或者实例本身调用
    Emplayee.get_sex()
    emplayee.get_sex()