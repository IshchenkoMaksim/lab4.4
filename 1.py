#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, которая запрашивает ввод двух значений. Если хотя бы
одно из них не является числом, то должна выполняться конкатенация, т.е.
соединение, строк. В остальных случаях введенные числа суммируются.
"""


class Summa:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print("Результат: ", int(self.a) + int(self.b))

    def con(self):
        print("Результат: ", self.a + self.b)


def main():
    a = input("Первое значение: ")
    b = input("Второе значение: ")
    result = Summa(a, b)
    try:
        result.add()
    except ValueError:
        result.con()


if __name__ == "__main__":
    main()
