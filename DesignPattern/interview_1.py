# coding: utf-8

"""
需求描述
1, Frisk工厂可以生产许多不同类型的笔，比如 铅笔，钢笔
2，所有的笔都可以写字，可以写到不同的载体上，如 纸，玻璃
3，不是所有的笔都能往所有的载体上写字，比如钢笔就无法写到玻璃上
4，有些载体上写的内容是可以擦除的（取决于用什么笔去写，例如马克笔在玻璃上可以擦除，但是写在纸上是不可以擦除的，铅笔无论在哪都可以擦除）
5，所有载体可写入的内容总量都是有上限的，超过容量后需要先擦除以前写的内容
6，每支笔都是消耗品，每次使用都会减少耐久度，不同的笔往不同的载体上写字会导致不同程度的损耗
7，笔的耐久程度为0后无法再使用，此时会被工厂进行回收


根据对以上需求的理解，给出代码架构设计，表达形式不限
要求：
1，架构尽可能优雅，不做过度设计
2，尽可能准确，简洁的

"""