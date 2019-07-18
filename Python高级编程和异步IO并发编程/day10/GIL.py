# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/17 上午10:30

"""
GIL: global interpreter lock(cpython存在)
    (GIL使得同一时刻只有一个线程在一个CPU上执行字节码)
"""
import threading

num = 0


def add():
    global num
    for i in range(1000000):
        num += 1


def remove():
    global num
    for i in range(1000000):
        num -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=remove)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(num)