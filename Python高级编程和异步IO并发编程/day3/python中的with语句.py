# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/11 上午10:13

"""
上下文管理器协议：实现__enter__,__exit__方法
"""

class DoWith(object):

    def __enter__(self):
        print('enter')  # 类似获取资源
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')  # 类似释放资源

    def do_somethong(self):
        print('do something')  # 操作资源


if __name__ == '__main__':
    with DoWith() as dowith:
        dowith.do_somethong()