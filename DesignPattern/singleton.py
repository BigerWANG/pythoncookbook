# coding: utf-8


"""
单例模式

保证一个类只有一个实例，并提供一个访问它的全局访问点
优点：
1, 对唯一实例的受控访问
2，当离相当于全局变量，但防止了命名空间被污染

一般情况下，设计以简单工单模式或者工厂方法模式开始，当你发现设计需要更大的灵活性时，则向更复杂的设计模式演化

"""


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        """重写new方法，new是生成实例之前被调用的方法"""
        if not hasattr(cls, "_instance"):  # 先看是不是有new方法
            # 如果没有new方法，则调用父类的new方法去创建实例
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MySingleton(Singleton):
    def __init__(self, a):
        self.a = a


class MySingleton1(Singleton):
    def __init__(self, b):
        self.b = b


a = MySingleton("a")
b = MySingleton("b")  # b 会指向a 因为使用了单例模式


print a.a
print b.a

print a is b
