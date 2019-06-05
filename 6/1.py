# -*- coding: utf-8 -*-

'''
1. Подсчитать, сколько было выделено памяти
под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат
и определить программы с наиболее эффективным использованием памяти.
'''
from pympler.asizeof import asizeof 
from memory_profiler import profile
from sys import getrefcount, getsizeof
from math import log, sqrt
from random import randint

# python -V - 3.7.2; platform.architecture - 32bit

def clear_screen():
    from os import system, name 
    system('cls') if name == 'nt' else system('clear')

##################################
# Вычисление n-го простого числа #
##################################

@profile
def i_prime(n):
    check_number = 1
    while n > 0:
        check_number += 1
        if check_number != 2 and check_number % 2 == 0:
            continue
        divider = 2
        is_prime = True
        while divider * divider <= check_number:
            if check_number % divider == 0:
                is_prime = False
                break
            divider += 1
        if is_prime:
            n -= 1 
    vars_RAM =  asizeof(check_number) +\
                asizeof(n) +\
                asizeof(divider) +\
                asizeof(is_prime)
    #print(vars_RAM) # при 1000-м простом числе 64B
    return check_number


# изменил первоначальный алгоритм, реализовал классическое решето с определением диапазона.
# в такой реализации алгоритм однозначно на больших числах работает быстрее наивного.
@profile
def ert_i_prime(n):
    rng = n
    while rng / log(rng) < n:
        rng += 1

    list_of_nums = [0] * rng

    for i in range(rng):
        list_of_nums[i] = i

    list_of_nums[1] = 0

    sieve = 2
    while sieve < rng:
        if list_of_nums[sieve] != 0:
            next_num_idx = sieve * 2
            while next_num_idx < rng:
                list_of_nums[next_num_idx] = 0
                next_num_idx += sieve
        sieve += 1

    list_of_primes = [num for num in list_of_nums if num != 0]
    vars_RAM =  asizeof(rng) +\
                asizeof(n) +\
                asizeof(list_of_nums) +\
                asizeof(sieve) +\
                asizeof(next_num_idx) +\
                asizeof(list_of_primes) +\
                asizeof(i)
    #print(vars_RAM) # при 1000-м простом числе 77 KiB
    del list_of_nums
    return list_of_primes[n - 1]

i_prime(1000)
ert_i_prime(1000)

'''
Производился поиск 100, 1000 и 10000 простого числа.
memory Profiler указывает, что в первой функции используется 11.3 MiB RAM,
при этом не наблюдается инкрементов по ходу исполнения программы. При
использовании решета Эратосфена интерпретатор выделяет 11.4 МБ RAM,
инкремент появился на 10000 простом числе и составил 0.4 MiB. Общая потребляемая память
второго алгоритма составила 13.7 MiB. Применение инструкции del не оказало влияния
на потребляемую память, на сколько понимаю, это связано с тем,
что выделенной памяти хватило. Кроме того, использование не примитивов
сильно сказывается на занимаемой памяти (Первый алгоритм 64 Byte, второй - 77 KiB)
 
Дополнительно, можно заметить, что на каждый цикл
for интерпретатор выделяет незначительный объем памяти,
по всей видимости, это связано с особенностями объявления и использования при каждой
итерации переменной. Поэтому, можно предположить, что при увеличении числа
итераций, увеличивается потребляемая память. Кроме того, заметно, что
в целом увеличение скорости вычислений способствует увеличению потребляемой
памяти.
'''
input('press anykey: ')
clear_screen()

##############################################################
# Поиск наибольшего числа среди наименьших в ячейках матрицы #
##############################################################

@profile
def matrix_generator(q_of_rows, q_of_cels):
    matrix = [[0] * q_of_cels for x in range(q_of_rows)]
    for row in matrix:
        idx = 0
        for cell in row:
            row[idx] = randint(1, 100)
            idx += 1
    vars_RAM =  asizeof(matrix) +\
                asizeof(row) +\
                asizeof(idx) +\
                asizeof(cell)
    #print(vars_RAM) # 1.3 KiB
    return matrix


@profile
def max_of_mins_in_matrix(matrix):
    i = 0
    j = 0
    min_num_in_cell = float('inf')
    max_of_inferior = float('-inf')
    while j < len(matrix[i]):
        while i < len(matrix):
            min_num_in_cell = matrix[i][j] if matrix[i][j] < min_num_in_cell else min_num_in_cell
            i += 1
        max_of_inferior = min_num_in_cell if max_of_inferior < min_num_in_cell else max_of_inferior
        min_num_in_cell = float('inf')
        i = 0
        j += 1
    vars_RAM =  asizeof(i) +\
                asizeof(j) +\
                asizeof(matrix) +\
                asizeof(min_num_in_cell) +\
                asizeof(max_of_inferior)
    # print(vars_RAM) # 1.023 KiB
    return max_of_inferior

clear_screen()

q_of_rows = 500 # asizeof = 16 B
q_of_cels = 500 # asizeof = 16 B

matrix = matrix_generator(q_of_rows, q_of_cels) # asizeof = 1023 KiB
result = max_of_mins_in_matrix(matrix) # asizeof = 16 B

'''
Касательно переменных:
первоначально выделено по 16 B для переменных q_of_rows и q_of_cels;
далее при выполнении первой функции выделено 1.3 KiB (по исполнению 
переменные кроме matrix очищены), результат присвоен nonlocal matrix = 1.023 KiB
при выполнении второй функции выделен 1.023 KiB, результат присвоен nonlocal
переменной 16 B.
при вызове функции matrix_generator(500, 500) интерпретатор выделил 12.3 MiB RAM.
при использовании генераторного выражения память инкрементирована на 0.1 MiB
Общая потребляемая память составила 13.4 MiB. Указанный размер памяти был выделен
для выполнения второй функции, в ходе исполнения она не инкрементировалась.
'''

input('press anykey: ')
clear_screen()