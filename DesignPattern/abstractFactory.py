# coding: utf-8

"""
抽象工厂模式

定义一个工厂类接口，【让工厂子类来创建一系列相关或相互依赖的对象】
相比工厂方法，抽象工厂模式中的每个具体工厂都生产一套产品(多个)

抽象工厂其实就是替客户端调用多个类进行拼装 然后再返回给客户端的方法

优点：
1，规范客户端行为
2，解耦客户端操作，将客户端与类的具体实现相分离
3，每个工厂创建了一个完整的产品系列，使得客户端易于交换产品系列
4，有利于产品的一致性

缺点：
对新种类的产品抽象不友好


"""

from abc import ABCMeta, abstractmethod

# -----抽象工厂------


class PhoneFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


class CPUFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def show_cpu(self):
        pass


class ShellFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def show_shell(self):
        pass


class OSFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def show_os(self):
        pass

# --------抽象具体实现----------


class LianfakeCPU(CPUFactory):
    def show_cpu(self):
        print "联发科cpu"


class IntelCPU(CPUFactory):
    def show_cpu(self):
        print "Intel cpu"


class IOS(OSFactory):
    def show_os(self):
        print "IOS"


class Android(OSFactory):
    def show_os(self):
        print "Android"


class MetalShell(ShellFactory):
    def show_shell(self):
        print "metal shell"


class PlasticShell(ShellFactory):
    def show_shell(self):
        print "plastic shell"


class HuaweiPhone(PhoneFactory):
    def make_shell(self):
        return PlasticShell()

    def make_os(self):
        return Android()

    def make_cpu(self):
        return LianfakeCPU()


class IPhone(PhoneFactory):
    def make_shell(self):
        return MetalShell()

    def make_os(self):
        return IOS()

    def make_cpu(self):
        return IntelCPU()


# ----客户端------

class Phone(object):
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def phone_info(self):
        print "手机信息："
        self.os.show_os()
        self.cpu.show_cpu()
        self.shell.show_shell()


def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)

huawei = make_phone(HuaweiPhone())

huawei.phone_info()


