# -*- coding: utf-8 -*-

'''
6. В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

'''
Данная задача также двусмыслена:
1. Имеется в виду, что необходимо сначала минимальные и максимальные эл-ы найти, а затем сумму всех эл-в между ними
2. Или произвольно указать границы.

Сделаю в двух вариантах.
'''

from random import random

source_list = [0] * (int(random() * (10 - 5) + 5)) 
source_list = [int(random() * 101) for x in source_list]
print(source_list)

# Не пользуюсь встроенными функциями max, min и методом index

# 1 

max_num = float('-inf')
max_index = 0
min_num = float('inf')
min_index = 0
for i in range(len(source_list)):
	if source_list[i] > max_num:
		max_num = source_list[i]
		max_index = i
	if source_list[i] < min_num:
		min_num = source_list[i]
		min_index = i

print(f'Мaксимальное число: {max_num}, индекс {max_index}')
print(f'Минимальное число: {min_num}, индекс {min_index}')

if min_index > max_index:
	max_index, min_index = min_index, max_index

sum_of_nums = 0
for i in range(min_index + 1, max_index):
	sum_of_nums += source_list[i]

print(f'сумма элементов между max, min: {sum_of_nums}')

# 2
min_index = int(input('Укажите начальный индекс: '))
max_index = int(input('Укажите максимальный индекс: '))

if min_index > max_index:
	max_index, min_index = min_index, max_index

sum_of_nums = 0
for i in range(min_index + 1, max_index):
	sum_of_nums += source_list[i]
print(f'сумма элементов между max, min: {sum_of_nums}')	
