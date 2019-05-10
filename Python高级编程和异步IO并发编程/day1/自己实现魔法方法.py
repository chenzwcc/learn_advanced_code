# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/3/26 上午9:13
import bisect
from collections import deque


class Company(object):
    def __init__(self, list_data):
        self.employee = list_data

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

inter_list = deque()
bisect.insort(inter_list,2)
print(inter_list)

if __name__ == '__main__':
    pass
    # company = Company([1, 2, 3])
    # # print('company',company,type(company),len(company))
    # print(hasattr(company,'__len__'))
    # for item in company:
    #     print(item)
