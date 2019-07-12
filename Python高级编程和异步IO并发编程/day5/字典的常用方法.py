# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/12 下午1:56

import copy

dict1 = {"chen":{"sex":"male"}}

new_dict = copy.copy(dict1)

new_dict["chen"]["sex"] = "female"

print(new_dict)

