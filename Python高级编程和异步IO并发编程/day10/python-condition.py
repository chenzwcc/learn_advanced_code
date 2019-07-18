# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/17 下午4:50

"""
线程间同步之条件变量Condition
"""
import threading
import time

con = threading.Condition()

num = 0


# 生产者
class Producer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # 锁定线程
        global num
        con.acquire()
        while True:
            print("开始添加！！！")
            num += 1
            print("火锅里面鱼丸个数：%s" % str(num))
            time.sleep(1)
            if num >= 5:
                print("火锅里面里面鱼丸数量已经到达5个，无法添加了！")
                # 唤醒等待的线程
                con.notify()  # 唤醒小伙伴开吃啦
                print('233333')
                # 等待通知
                con.wait()
                print('2222')
        # 释放锁
        con.release()


# 消费者
class Consumers(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        con.acquire()
        global num
        while True:
            print("开始吃啦！！！")
            num -= 1
            print("火锅里面剩余鱼丸数量：%s" % str(num))
            time.sleep(2)
            if num <= 0:
                print("锅底没货了，赶紧加鱼丸吧！")
                con.notify()  # 唤醒其它线程
                print('0000')
                # 等待通知
                con.wait()
        con.release()


p = Producer()
c = Consumers()
p.start()
c.start()
