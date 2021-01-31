# coding: utf-8

"""
适配器模式
将一个类的接口转换成客户希望的另一个接口，适配器模式使得原本不兼容的而不能一起工作的类能够一起工作

两种实现方式：
1，多继承
2，组合
"""


def memcpy(data):
    """
    实现一个深拷贝
    :param data:
    :return:
    """
    if not data:
        return data

    copy_data = data

