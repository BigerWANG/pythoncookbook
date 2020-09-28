# coding: utf-8

"""
工厂表示负责创建其他类型对象的类

工厂模式的优点：
1，松耦合，即对象的创建可以独立于类的实现
2，客户端无需了解创建对象的类，但是照样可以使用工厂来创建对象
3，客户端只需要知道需要传递的接口方法和参数
4，
Factory
simple Factory
"""

from abc import ABCMeta, abstractmethod


# 简单工厂模式：可以为客户端创建不同的对象，如不是将对象实例化
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("wo wo")


class Cat(Animal):
    def do_say(self):
        print("Miao Miao")

class Factory:
    @classmethod
    def make_sound(cls, Animal):
        return eval(Animal)().do_say()

Factory.make_sound("Dog")


# 工厂方法模式：

