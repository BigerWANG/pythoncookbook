# coding: utf-8

"""
<<<<<<< HEAD
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

=======
工厂方法模式

定义一个用于创建对象的接口(工厂接口)，让子类决定实例化哪一个产品类

角色：
抽象工厂角色(Creator) 1
具体工厂角色 n

抽象产品角色
具体产品角色

优点：
每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
隐藏了对象创建的实现细节

缺点：
每增加一个具体产品类，就需要增加一个相应的具体工厂类，比较繁琐
"""
from abc import ABCMeta, abstractmethod


class Pay(object):  # 抽象产品
    __metaclass__ = ABCMeta

    @abstractmethod
    def pay(self, s):
        pass


class Ailpay(Pay):  # 具体的产品
    def pay(self, s=0):
        print "支付宝支付", s, "元"


class WeChatPay(Pay):
    def pay(self, s=0):
        print "微信支付", s, "元"


class BankPay(Pay):
    def pay(self, s=0):
        print "银行卡支付", s, "元"


class PaymentFactory(object):  # 抽象工厂类，它的子类去决定具体创建那个类
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_payment(self):
        pass


class AilpayFactory(PaymentFactory):  # 子类决定去具体创建哪个类
    def create_payment(self):
        return Ailpay()


class WeChatFactory(PaymentFactory):
    def create_payment(self):
        return WeChatPay()


class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


#  client

p = WeChatFactory().create_payment()

p1 = BankPayFactory().create_payment()


p.pay(100)
p1.pay(5)
>>>>>>> 9a1e4bc5a30bb9f7efa01ca2461625f0a5e109cb
