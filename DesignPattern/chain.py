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
    """定义一个接口"""
    __metaclass__ = ABCMeta

    def __new__(cls, *args, **kwargs):
        # 判断实例中是否有instance字段
        if not hasattr(cls, "_instance"):
            cls._instance = super(Handle, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def set_next(self, handle):
        pass

    def handle(self, req):
        pass


class AbsHandler(Handle):
    __next_handle: Handle = None

    def set_next(self, handle):
        self.__next_handle = handle
        return handle

    @abstractmethod
    def handle(self, req):
        if self.__next_handle:
            return self.__next_handle.handle(req)
        return



class DirctLeader(AbsHandler):

    def handle(self, day):
        if day <= 3:
            print("this {} request will be OK".format(day))
            return
        else:
            print("DirctLeader cant handle")
            return super().handle(day)


class DeapartmentManager(AbsHandler):

    def handle(self, day):
        if day <= 10:
            print("this {} request will be OK".format(day))
        else:
            print("DeapartmentManager cant handle")
            return super().handle(day)


class Boss(AbsHandler):
    def handle(self, day):
        if day <= 10:
            print("this {} request will be OK".format(day))
            return
        else:
            print("fuck off")
            return super().handle(day)


def client(handler):
    day = 100
    handler.handle(day)



if __name__ == '__main__':
    # 把责任链条连起来
    chain = [DirctLeader(), DeapartmentManager(), Boss()]
    chain = (i for i in chain)
    head = next(chain)
    while 1:
        try:
            obj = next(chain)
            head.set_next(obj)
            head = obj
        except StopIteration:
            break
    l = DirctLeader()
    client(l)




