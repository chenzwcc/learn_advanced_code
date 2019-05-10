# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/5/10 下午2:55
"""
函数和类也是对象，属于python的一等公民

一等公民(解释): 1.可以赋值给一个变量。详见注解一
              2.可以添加到集合列表中。详见注解二
              3.可以作为参数传递给函数。详见注解三
              4.可以做函数的返回值。详见注解四
"""


class CusotmClass:
    def __init__(self):
        print('类可以赋值给变量')


def func(*args, **kwargs):
    print('函数可以赋值给变量', args, kwargs)


def func2(*args, **kwargs):
    return args, kwargs


if __name__ == '__main__':
    # 注解一
    var1 = func
    var2 = CusotmClass

    var1()
    var2()
    print(type(var1), type(var2))

    # 注解二
    obj_list = []
    obj_set = set()

    obj_list.append(func)
    obj_list.append(CusotmClass)
    print(obj_list)

    obj_set.add(func)
    obj_set.add(CusotmClass)
    print(obj_set)

    # 注解三
    func(CusotmClass)

    # 注解四
    return_value = func2(func)
    print(return_value)
