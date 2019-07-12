# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/12 上午11:08

"""
列表推导式: 用过一行代码完成列表(列表生成式性能较高)

"""

# 列表推导式
list1 = [i for i in range(1, 21) if i % 2]
print(list1)

# 生成器表达式
generator1 = (i for i in range(1,  20) if i % 2)
print(type(generator1))

# 字典推导式
dict1 = {key: val for key, val in enumerate(['kye1', 'key2', 'key3'])}
print(dict1)
