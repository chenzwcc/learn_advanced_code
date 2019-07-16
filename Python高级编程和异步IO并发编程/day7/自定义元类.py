# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/15 下午3:59

"""

"""

Student = type('Student', (object,), {'name': "chenzecc"})

stu1 = Student()
print(getattr(stu1, 'name', None))


def __init__(self, name):
    self.name = name


def test(self):
    print('0000')


People = type('People', (object,), {"__init__": __init__, "test": test})
people = People("chenzw")
print(people.name)
people.test()


class Base(object):
    pass


class NewBase(Base):
    foo = True


Foo = type('Foo', (NewBase,), {'foo': False})

foo = Foo()
print(foo.foo)


class ModelMetaClass(type):

    def __new__(cls, class_name, class_parents, class_attrs):
        print(class_name, class_parents, class_attrs)
        mapping = dict()

        for name, value in class_attrs.items():
            if isinstance(value, tuple):
                print("Found mapping %s --> %s" % (name, value))
                mapping[name] = value

        for name in mapping.keys():
            class_attrs.pop(name)

        class_attrs["__mapping__"] = mapping
        class_attrs["__table__"] = class_name

        return type.__new__(cls, class_name, class_parents, class_attrs)


class User(metaclass=ModelMetaClass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        fields = []
        args = []

        for k, v in self.__mapping__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))

        sql = "insert into %s(%s) values(%s)" % (self.__table__, ",".join(fields), ",".join([str(i) for i in args]))
        print("SQL: %s" % sql)


# u = User(uid=123, name="zfx", email="zfx@zfx.com", password="6666")
# u.save()


class A(type):
    def __new__(cls, class_name, class_parents, class_attrs):
        print(class_name, class_parents, class_attrs)
        return type.__new__(cls, class_name, class_parents, class_attrs)


class B(metaclass=A):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


b = B(x=1)













