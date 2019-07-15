# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/15 上午9:05

"""
之所以导致经典的原因在于staffs对象是否是可变类型，如果是，则staffs在每个实例化的对象之间共享，
如果不是，staffs在每个实例化的对象后都是独立的。

默认参数可以通过 class.__init__.__defaults__获取。
"""


class Company1:
    def __init__(self, name, staffs=()):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs = self.staffs.__add__(staff_name)


class Company2:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)


if __name__ == "__main__":
    com1 = Company1("com1")
    com1.add(("com1",))
    print(Company1.__init__.__defaults__)  # ((),)
    com2 = Company1("com2")
    com2.add(("com2",))
    print(Company1.__init__.__defaults__)  # ((),)
    print(com1.staffs is com2.staffs)  # False

    com3 = Company2("com3")
    com3.add("com3")
    print(Company2.__init__.__defaults__)  # (['com3'],)
    com4 = Company2("com4")
    com4.add("com4")
    print(Company2.__init__.__defaults__)  # (['com3', 'com4'],)
    print(com3.staffs is com4.staffs)  # True


