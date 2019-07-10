# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/10 上午11:20

"""
私有属性的含义是外部不能直接用 实例名.私有属性名进行访问，子类同样也是一样不能访问， 这样就是对数据进行封装。
只能用公共的方法里调用私有属性。不过也可以通过 实例名._类名__私有属性名调用。

私有属性定义：在属性名称前加上双下划线或者单下划线，
            单下划线：只是告诉别人这是私有属性，外部依然可以通过实例对象访问也能被继承
            双下划线：不能被继承不能被实例对象访问
"""


class DateBase(object):

    def __init__(self, x, y):
        self._x = x
        self.__y = y

    def __get_name(self):
        print("this is a private mothed")

    def get__get_name(self):
        self.__get_name()


class Date(DateBase):
    pass


if __name__ == '__main__':
    datebase = DateBase(1, 2)
    datebase.__get_name()  # AttributeError: 'DateBase' object has no attribute '__get_name'
    datebase.get__get_name()  # this is a private mothed
    print(datebase._x)  # 1
    print(datebase.__y)  # AttributeError: 'DateBase' object has no attribute '__y'

    datebase._DateBase__get_name()  # 通过实例访问累的私有属性

    date = Date(1, 2)
    date.__get_name()  # AttributeError: 'Date' object has no attribute '__get_name'

    print(date._x)  # 单下划线能被继承
    print(date.__y)  # 双下划线不能被继承
