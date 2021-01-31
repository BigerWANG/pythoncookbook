# coding: utf-8

"""
观察者模式（发布-订阅模式）：

定义对象一种一对多的依赖关系，当一个对象(发布者)的状态发生改变时，所有依赖于它的对象(订阅者)都得到通知并且被自动更新





适用场景：
当一个抽象模型有两方面，其中一方面依赖于另一方面，将这两者封装在独立的对象中使得他们可以独立的改变和复用

当对一个对象的改变需要同时改变其他对象，并且不知道具体有多少对象待改变时

当一个对象必须通知其他对象，而它又不能假定其他对象是谁。换言之，你不希望这些对象是是紧耦合的

优点：
发布者和订阅者之间松耦合
支持广播订阅


"""

from abc import ABCMeta, abstractmethod


# 定义一个观察者(订阅者)接口

class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, notice):
        pass


# 定义一个发布者的父类
class Notice(object):
    def __init__(self):
        self.observers = []  # 保存它的订阅者

    def attach(self, obs):
        """添加新的订阅者"""
        self.observers.append(obs)

    def deattch(self, obs):
        """解除订阅者"""
        self.observers.remove(obs)

    def notice(self):
        """向订阅者发送通知"""
        for abs in self.observers:
            abs.update(self)  # 这一步是将发布者自己传进来，使得订阅者直接调用自己的属性


class StaffNotice(Notice):
    """发布者对象的子类 具体的发布者"""
    def __init__(self, notice_info=None):
        super(StaffNotice, self).__init__()
        self.__notice_info = notice_info

    @property
    def notice_info(self):
        return self.__notice_info

    @notice_info.setter  # 当info状态改变时对订阅者进行通知
    def notice_info(self, notice_info):
        self.__notice_info = notice_info
        self.notice()


class Staff(Observer):
    def __init__(self):
        self.info = None

    def update(self, notice):
        self.info = notice.notice_info  # 将通知的内容更新到自己的属性中


if __name__ == '__main__':
    s1 = Staff()
    s2 = Staff()

    notice = StaffNotice()
    notice.attach(s1)
    notice.attach(s2)
    notice.notice_info = "hahahah！！"
    notice.deattch(s2)
    notice.notice_info = "明天放假啦"
