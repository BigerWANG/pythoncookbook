# coding: utf-8

"""
代理模式
为其他对象提供一种代理以控制对这个对象的访问
应用场景：
远程代理： 为远程的对象提供代理
虚拟代理：根据需要创建很大的对象
保护代理：控制对原始对象的访问，适用于对象有不同的访问权限时

"""

from abc import ABCMeta, abstractmethod


class PremissionError(Exception):
    pass


class SubJect(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def read_conetent(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealJect(SubJect):

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, "r") as f:
            self.content = f.read()

    def read_conetent(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, "w") as f:
            f.write(content)


class SubJectProxy(SubJect):

    def __init__(self, filename):
        self.filename = filename
        self.real = None

    def read_conetent(self):
        if not self.real:
            self.real = RealJect(self.filename)
        return self.real.read_conetent()

    def set_content(self, content):
        if not self.real:
            self.real = RealJect(self.filename)
        self.real.set_content(content)


class ReadProxy(SubJect):
    def __init__(self, filename):
        self.filename = filename
        self.real = None

    def read_conetent(self):
        if not self.real:
            self.real = RealJect(self.filename)
        return self.real.read_conetent()

    def set_content(self, content):
        raise PremissionError("have not set permission")


reader = ReadProxy("test.txt")
print reader.read_conetent()
reader.set_content("xxxsadsa")
