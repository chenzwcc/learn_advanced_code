# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/5/10 下午4:13
"""
项目定义空变量是该用为None，因为全局都会指向同一个内存地址，所以不会造成内存浪费

"""
a = None
b = None
print(id(a),id(b))

