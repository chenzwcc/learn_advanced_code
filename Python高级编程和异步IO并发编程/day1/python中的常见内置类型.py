# _*_coding:utf-8_*_

# 创建用户  ：chenzhengwei

# 创建日期  ：2019/5/10 下午4:13

"""
python中的常见内置类型:(1) 对象的三个特征:1）身份：在内存中的地址(通过id查询)。 2）类型。 3）值。
                     (2) None。
                     (3) 数值  :1) int。:2) float。:3) complex (复数)。:4) bool。
                     (4) 迭代类型。
                     (5) 序列类型 :1) list。:2) range :3) tuple :4) str :5) array :6) 二进制序列。
                     (6) 映射(dict)。
                     (7) 集合。
                     (8) 上下文管理类型(with)。
                     (9) 其他。
"""

"""
项目定义空变量是该用为None，因为全局都会指向同一个内存地址，所以不会造成内存浪费

"""
a = None
b = None
print(id(a),id(b))

