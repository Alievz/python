# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.

from itertools import count
from itertools import cycle


def count_func(start, stop):
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)


def cycle_func(list, iteration):
    i = 0
    iter = cycle(list)
    while i < iteration:
        print(next(iter))
        i+=1


count_func(start = int(input("Введите начальное число: ")), stop = int(input("Введите конечное число: ")))
cycle_func(list = [1, 2], iteration = int(input("Введите количество итераций: ")))