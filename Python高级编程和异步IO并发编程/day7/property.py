# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/15 上午10:28

"""
property:动态属性，保护某些属性不被直接修改
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
        self._age = value


if __name__ == '__main__':
    perple = People('chen')
    print(perple.age)
    perple.set_age = 20
    print(perple.age)
