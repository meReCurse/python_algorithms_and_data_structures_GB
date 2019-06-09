# -*- coding: utf-8 -*-

'''
Задание 2:
Отсортируйте по возрастанию методом слияния
одномерный вещественный массив, заданный случайными
числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''
from random import uniform, randint

def merge_sort(lst):
    '''
    Реализация алгоритма сортировки слиянием.
    :param lst: list of nums
    :return: sorted not same lst (asc) 
    '''
    def merge(left, right):
        '''
        Функция реализует фазу слияния разделенных списков.
        :param left: list of nums
        :param right: list of nums
        :return: merged list
        '''
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def split(lst):
        '''
        Функция реализует фазу разделения списков.
        Рекурсивно разделяет подсписки. 
        :param lst: list of nums
        :return: вызывает функцию слияния
        '''
        if len(lst) < 2:
            return lst
        middle = len(lst) // 2
        left = split(lst[:middle])
        right = split(lst[middle:])
        return merge(left, right)

    return split(lst)

if __name__ == '__main__':
    rng = randint(11, 21)
    lst = [round(uniform(0, 49), 2) for _ in range(rng)]
    print(f'source: {lst}')

    lst_ord = merge_sort(lst)
    print(f'sorted: {lst_ord}')