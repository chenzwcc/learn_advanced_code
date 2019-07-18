# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/17 上午11:15
import threading
import time
from queue import Queue

q = Queue(10)


def get_num():
    while True:
        if not q.empty():
            print("---get a num:%s---" % q.get())
        else:
            print("---please waiting,queue is empty---")
            time.sleep(2)


def set_num():
    while True:
        if not q.full():
            print("---set a num:1---")
            q.put(1)
        else:
            print("---please waiting,queue is full---")
            time.sleep(2)


if __name__ == '__main__':
    thread1 = threading.Thread(target=get_num)
    thread2 = threading.Thread(target=set_num)
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()