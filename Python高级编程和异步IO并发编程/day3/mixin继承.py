# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/11 上午9:41

"""
Mixin编程是一种开发模式，是一种将多个类中的功能单元的进行组合的利用的方式。
"""


class Displayer(object):
    def display(self, message):
        print('3')
        print(message)


class LoggerMixin(object):
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        print('4')
        super().display(message)
        print('2',self)
        self.log(message)


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        print('1',self)
        super().log(message, filename='subclasslog.txt')


# print(MySubClass.mro())
# MySubClass ->(LoggerMixin,Displayer) ->object

subclass = MySubClass()
subclass.display("This string will be shown and logged in subclasslog.txt")
# 执行流程图在images/mixin继承.png

# 1.MySubClass.display()
# 2.第一步触发调用LoggerMixin的display方法，此方法调用super().display()，显然LoggerMixin类除了继承object类并没其他类，
#   也就没有display方法，于是就去寻找继承链，找到Display类中的display方法然后执行
# 3.LoggerMixin的display()方法继续调用self.log(),但是此时的self是指MySubClass的对象，因此调用MySubClass的log()方法
# 4.MySubClass.log()又调用super.log(),寻找继承链中的log(),找到LoggerMixin的log(),
# 5.执行LoggerMixin.log()