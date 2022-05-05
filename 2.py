#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Решите следующую задачу: напишите программу, которая будет генерировать матрицу
из случайных целых чисел. Пользователь может указать число строк и столбцов,
а также диапазон целых чисел. Произведите обработку ошибок ввода пользователя.
"""

import random


class Matrix:
    def __init__(self, line, column, range_min, range_max):
        self.line = line
        self.column = column
        self.range_min = range_min
        self.range_max = range_max

    def random_init(self):
        print([[random.randrange(self.range_min, self.range_max)
                for i in range(self.column)] for k in range(self.line)])


if __name__ == "__main__":
    try:
        line = int(input("Введите количество строк: "))
        column = int(input("Введите количество столбцов: "))
        range_min = int(input("Введите минимальную границу диапазона: "))
        range_max = int(input("Введите максимальную границу диапазона: "))
        matrix = Matrix(line, column, range_min, range_max)
        matrix.random_init()
    except ValueError:
        print("Ошибка при вводе значения")
