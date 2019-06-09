# -*- coding: utf-8 -*-

'''
Задача 1:
Отсортируйте по убыванию методом "пузырька"
одномерный целочисленный массив, заданный случайными
числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна
быть реализована в виде функции. По возможности
доработайте алгоритм (сделайте его умнее).
'''

from random import randint
from timeit import timeit


def bubble_sort(arr):
    '''
    Реализация сортировки пузырьком
    :param arr: list of nums
    :return: sorted same list (asc) 
    '''
    n = len(arr)
    for i in range(1, n):
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_opt(arr):
    '''
    Оптимизация сортировки пузырьком,
    через проверку осуществления перестановок
    на шаге итерации.
    :param arr: list of nums
    :return: sorted same list (asc) 
    '''
    n = len(arr)
    for i in range(1, n):
        is_shift = False
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_shift = True
        if not is_shift:
            break
    return arr


def bubble_sort_opt2(arr):
    '''
    Оптимизация сортировки пузырьком,
    через запоминание последней позиции
    перестановки.
    :param arr: list of nums
    :return: sorted same list (asc) 
    '''
    n = len(arr)
    while n > 1:
        shift = 0
        for j in range(1, n):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                shift = j
        n = shift
    return arr

arr = [randint(-100, 99) for _ in range(randint(10, 100))]
print(f'array: {arr}\n')

time = timeit('bubble_sort(arr.copy())', setup='from __main__ import bubble_sort, arr', number=1000)
print(f"{bubble_sort.__name__}: {time}\n")
print(f'{bubble_sort(arr.copy())}\n')

time = timeit('bubble_sort_opt(arr.copy())', setup='from __main__ import bubble_sort_opt, arr', number=1000)
print(f"{bubble_sort_opt.__name__}: {time}\n")
print(f'{bubble_sort_opt(arr.copy())}\n')

time = timeit('bubble_sort_opt2(arr.copy())', setup='from __main__ import bubble_sort_opt2, arr', number=1000)
print(f"{bubble_sort_opt2.__name__}: {time}")
print(f'{bubble_sort_opt2(arr.copy())}\n')
