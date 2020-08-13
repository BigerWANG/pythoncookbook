# coding: utf-8

"""
责任链模式


概念
在责任链模式中，一个任务由多个对象进行处理，多个对象之间是递进关联的关系。直到某一个对象处理完成才结束

优点：
解耦调用方和处理方，调用方只需要将任务发送给处理方，由处理方完成内部的链式传递并返回结果
"""

from abc import ABCMeta, abstractmethod


class Handle(object):
    """定义一个借口"""
    __metaclass__ = ABCMeta
    @abstractmethod
    def request_leave(self, day):
        pass


class DirctLeader(Handle):
    def __init__(self):
        self.next_hanle = DeapartmentManager()

    def request_leave(self, day):
        if day <= 3:
            print "this {} request will be OK".format(day)
        else:
            self.next_hanle.request_leave(day)


class DeapartmentManager(Handle):
    def __init__(self):
        self.next_hanle = Boss()

    def request_leave(self, day):
        if day <= 10:
            print "this {} request will be OK".format(day)
        else:
            self.next_hanle.request_leave(day)


class Boss(Handle):
    def request_leave(self, day):
        if day <= 10:
            print "this {} request will be OK".format(day)
        else:
            print "you are fired!! "





def test():
    day = 100

    DirctLeader().request_leave(day)

if __name__ == '__main__':
    test()