# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/16 下午4:14

"""
    迭代器原理：只需要在类的__iter__方法中返回一个对象自身，这个对象拥有一个next()方法，这个方法能不断返回下一个值并在恰当的时候抛出StopIteration异常即可
"""


# 自定义迭代器


class CustomIteration(object):

    def __init__(self, data_list):
        self.data_list = data_list
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < len(self.data_list):
            self.num += 1
            return self.data_list[self.num - 1]
        else:
            raise StopIteration


"""
    生成器的编写方法和函数定义类似，只是在return的地方改为yield,当生成器遇到一个yield时，会暂停运行生成器，
    返回yield后面的值。当再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield
"""


def func():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    a = CustomIteration([1, 2, 3])
    print(type(a), a)
    for i in a:
        print(i)

    for i in func():
        print(i)

