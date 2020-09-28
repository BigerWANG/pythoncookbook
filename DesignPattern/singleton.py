# coding: utf-8


"""
单例模式

保证一个类只有一个实例，并提供一个访问它的全局访问点
优点：
1, 对唯一实例的受控访问
2，当离相当于全局变量，但防止了命名空间被污染

一般情况下，设计以简单工单模式或者工厂方法模式开始，当你发现设计需要更大的灵活性时，则向更复杂的设计模式演化

应用场景：
单例模式具有整体性，统一性的优势，适用于以下场景：
1.资源管理的场景
2.难以同步的场景
3.涉及共享的场景
4.有关认证的场景，设置一个统一认证的类，只需认证一次，随处调用即可
"""

from threading import Lock, Thread

import time


def synchronized(func):
    # 线程安全的装饰器
    def lock_func(*args, **kwargs):
        with Lock():
            return func(*args, **kwargs)
    return lock_func


class Singleton(object):
    # 重写new方法
    @synchronized
    def __new__(cls, *args, **kwargs):
        # 判断实例中是否有instance字段
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Singleton1(object):
    _instance_lock = Lock()

    def __init__(self, *args, **kwargs):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        with Singleton1._instance_lock:
            if not hasattr(Singleton1, "_instance"):
                Singleton1._instance = Singleton1(*args, **kwargs)
            return Singleton1._instance


class MyClass(Singleton):
    pass


def task(arg):
    obj = MyClass()


if __name__ == "__main__":
    # a = Singleton(3)
    # print("a单例! id为 %s" % id(a))
    # b = Singleton(4)
    # print("b单例! id为 %s" % id(b))
    # str = "hello world !"
    # c = Singleton(str)
    # print("c单例! id为 %s" % id(c))
    # print("ok!")
    num = 0
    l = [Thread(target=task, args=(i,)) for i in range(10)]
    for i in l:
        i.start()

