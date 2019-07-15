# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/15 上午11:01

"""

"""


class People(object):
    def __init__(self, x):
        self.x = x

    def __getattribute__(self, item):
        print('__getattribute__')
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print('getattr', item)
        return None


if __name__ == '__main__':
    people = People(2)
    # print(people.x)
    print(people.y)
    # print(help('__getattribute__'))
