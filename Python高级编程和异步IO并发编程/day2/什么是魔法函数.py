# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/5/10 下午4:59

"""
python中以双下划线开始并以双下划线结尾的函数即为魔法函数
"""


class CustomClass:

    def __init__(self, list_data):
        self.list_data = list_data

    def __getitem__(self, item):
        print(self.list_data[item], type(self.list_data[item]), item)
        return self.list_data[item]


my_class = CustomClass([1, 2, 3, 4])
for val in my_class:
    print(val)
