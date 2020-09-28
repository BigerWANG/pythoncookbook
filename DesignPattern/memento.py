# coding: utf-8

"""
备忘录模式

"""

from __future__ import annotations
import time
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters


class Memento(ABC):
    """
    备忘录抽象类
    """
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_state(self) -> str:
        pass


class Originator:
    """
    被保存状态的类
    """
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state  # 保存这个类的状态
        print(f"Originator: My inital state is: {self._state}")


    def do_something(self) -> None:
        """
        这个类要实现某些功能
        :return:
        """
        print("Originator: I'll do something")
        time.sleep(1)
        self._state = self.__generate_random_str(19)
        print("done...")

    @staticmethod
    def __generate_random_str(length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento):
        self._state = memento.get_state()
        print(f"Originator: My state has restore to:{self._state}")

    def show_state(self):
        print(self._state)


class ConcreteMemento(Memento):
    """
    备忘录抽象实例, 其实这就是个中间层, 为了使调用方不能直接访问到 源数据
    遵循了封闭原则
    """
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        return self._state

    def get_name(self):
        return f"{self._date} / {self._state[0:9]}..."

    def get_date(self):
        return self._date


class Caretaker:
    f"""
    备忘录功能实现者
    使用这个类实现对Originator的备份和回滚
    实现回滚和备份
    """

    def __init__(self, originator: Originator) -> None:
        self._memntos = []
        self._originator = originator


    def backup(self):
        """备份：将Originator保存到self._memtos中"""
        self._memntos.append(self._originator.save())

    def undo(self):
        """回滚：将Originator回滚到当前状态的上一个状态"""
        if not self._memntos:
            return
        mem = self._memntos.pop()
        self._originator.restore(mem)


    def show_history(self):
        for mem in self._memntos:
            print(mem.get_name())


if __name__ == '__main__':
    originator = Originator("No.1 version")
    caretaker = Caretaker(originator)
    caretaker.backup()

    originator.do_something()
    caretaker.backup()

    originator.do_something()
    caretaker.backup()


    caretaker.show_history()

    print("Now start rollback to the last version:\n")
    caretaker.undo()
    originator.show_state()
    time.sleep(1)

    caretaker.undo()
    originator.show_state()
    time.sleep(1)

    caretaker.undo()
    originator.show_state()
