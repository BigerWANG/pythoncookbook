# coding: utf-8

"""
设计原则之：多用组合少用继承
原因：
1，继承会造成代码的复杂度提高，想要了解子类的实现必须知道父类是如何实现的，违背封装的原则
2，继承层次过深，继承关系过于复杂会影响到代码的可读性和可维护性

"""


from  abc import ABCMeta, abstractmethod


class FlyAble(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class TweetAble(metaclass=ABCMeta):
    @abstractmethod
    def tweet(self):
        pass

class EggLayable(metaclass=ABCMeta):
    @abstractmethod
    def layegg(self):
        pass


class Ostrich(TweetAble, EggLayable):
    """
    这种方式也会造成代码的重复
    """
    def tweet(self):
        print("I can tweet")

    def layegg(self):
        print("I can lay egg")


class Sparrow(FlyAble, TweetAble, EggLayable):
    """
    这种方式也会造成代码的重复
    """
    def fly(self):
        print("I can fly")

    def tweet(self):
        print("I can tweet")

    def layegg(self):
        print("I can lay egg")


class FlyAbility(FlyAble):
    """先继承接口实现对应的具体的实现类，再使用组合的方式将实现类"""
    def fly(self):
        print("I can fly")



class TweetAbility(TweetAble):
    """先继承接口实现对应的具体的实现类，再使用组合的方式将实现类"""
    def tweet(self):
        print("I can tweet")


class EgglayAbility(EggLayable):
    """先继承接口实现对应的具体的实现类，再使用组合的方式将实现类"""
    def layegg(self):
        print("I can lay egg")



class NewOstrich:
    def __init__(self):
        self.__tweetability = TweetAbility()  # 组合
        self.__egglayability = EgglayAbility()

    def tweet(self):
        return self.__tweetability.tweet()  # 委托

    def egglay(self):
        return self.__egglayability.layegg() # 委托

if __name__ == '__main__':
    no = NewOstrich()

    no.tweet()
    no.egglay()



