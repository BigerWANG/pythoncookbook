# coding: utf-8

"""
命令模式

"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    command 抽象类生命一个 命令执行方法
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    简单命令实现
    """
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self):
        print(f"See I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    """
    复杂命令实现，不同的命令类型供不同的调用方使用
    """
    def __init__(self, receiver: Recevicer, a: str, b: str) -> None:
        """
           Complex commands can accept one or several receiver objects along with
           any context data via the constructor.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        """
        Commands can delegate to any methods of a receiver.
        """

        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Recevicer:
    """
    真正实现逻辑的类，它可以是任何类，由Command类调用
    """
    @staticmethod
    def do_something(a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)")

    @staticmethod
    def do_something_else(b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)")


class Invoker:
    """
    调用程序与一个或多个命令关联。它发送一个请求命令。
    """

    __on_start = None
    __on_finish = None

    """
    初始化命令
    """

    @property
    def on_start(self):
        return self.__on_start

    @on_start.setter
    def on_start(self, command: Command):
        self.__on_start = command


    @property
    def on_finish(self):
        return self.__on_finish

    @on_finish.setter
    def on_finish(self, command: Command):
        self.__on_finish = command


    def do_something_important(self) -> None:
        """调用者不依赖于具体的命令或接收者类别。的 调用方通过执行以下操作将请求间接传递给接收方命令。"""

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self.on_start, Command):
            self.on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self.on_finish, Command):
            self.on_finish.execute()


if __name__ == "__main__":
    """
    The client code can paramete
    """
    invoker = Invoker()
    receiver = Recevicer()
    invoker.on_start = SimpleCommand("Hello! ")

    invoker.on_finish = ComplexCommand(receiver, "send email", "do the report")
    invoker.do_something_important()


