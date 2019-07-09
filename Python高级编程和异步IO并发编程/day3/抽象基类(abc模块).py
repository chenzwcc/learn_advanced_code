# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/9 下午9:54

"""
某种情况下，判断某个对象是否具有某个属性或方法
"""


class Company(object):

    def __init__(self, emply_lists):
        self.emply_lists = emply_lists

    def __len__(self):
        return len(self.emply_lists)


company = Company(['a', 'b'])
print(len(company))

print(hasattr(company, '__len__'))
print(hasattr(company, 'get_emply'))

"""
某种情况下希望判定某个对象的类型
"""

from collections.abc import Sized

print(isinstance(company, Sized))

"""
如何模拟一个抽象基类
    抽象基类：1.不能被实例
             2.子类继承抽象基类必须实现抽象基类的方法   
"""
import abc


class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):

    def get(self, key):
        pass

    def set(self, key, value):
        pass


# cache = CacheBase()
redis_cache = RedisCache()
