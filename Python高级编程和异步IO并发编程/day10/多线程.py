# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/17 上午10:59

"""
对于IO操作，多线程与多进程性能差别不大，是因为在IO操作时多线程在等待时会主动让出资源供别的线程使用
        (可以通过注释time.sleep()观看代码执行顺序)。
"""

import threading
import time


def fun1():
    print('---fun1 start---')
    time.sleep(2)
    print("---fun1 end---")


def fun2():
    print('---fun2 start---')
    time.sleep(2)
    print("---fun2 end---")


if __name__ == '__main__':
    thread1 = threading.Thread(target=fun1)
    thread2 = threading.Thread(target=fun2)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()