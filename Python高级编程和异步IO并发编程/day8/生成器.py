# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/16 下午4:14

"""
生成器函数:只要函数内部包含yield关键字，那么这个函数就是生成器函数
"""


def func():
    yield 1
    yield 2
    yield 3
    yield 4


if __name__ == '__main__':
    fun = func()
    for i in fun:
        print(i)