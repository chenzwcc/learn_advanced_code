# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/11 下午4:21

"""
序列中的+，+=，extend的区别：
        +: 重新开辟一块内容空间存储两个序列的内容
        +=: 并没有开辟新空间，而是在原有基础上添加另一个序列的内容(注意：是任意序列类型)
        extend: 等价+=
"""
list1 = [1,2]
list2 = [3,4]
list3 = list1 + list2

# +
# print(id(list1),id(list2),id(list3))

# +=
# print(id(list1))
# list1 += list2
# print(id(list1))

# extend
print(id(list1))
list1.extend(list2)
print(id(list1))