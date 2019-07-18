# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/18 上午9:12

"""
进程间数据不共享，
"""
from multiprocessing import Process

num = 0


def fun1():
    global num
    for i in range(1000000):
        num += 1
    print("fun1 added num is {}".format(num), id(num))


def fun2():
    global num
    for i in range(1000000):
        num += 1
    print("fun2 added num is {}".format(num), id(num))


if __name__ == '__main__':
    process1 = Process(target=fun1)
    process2 = Process(target=fun2)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
