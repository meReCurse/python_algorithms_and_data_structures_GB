# -*- coding: utf-8 -*-

'''
3. В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.
'''

from random import random

# Создадим массив по условию, случайной длины, со случайными значениями

source_list = [0] * (int(random() * (10 - 5) + 5)) 
source_list = [int(random() * 101) for x in source_list]
print(source_list)

# при решении задачи, как и было сказано на уроке, ищу только первое вхождение, повторяющиеся числа не учитываю

i = 0
counter_max = float('-inf')
index_max = 0
counter_min = float('inf')
index_min = 0
while i < len(source_list):
	if source_list[i] > counter_max:
		counter_max = source_list[i]
		index_max = i
	if source_list[i] < counter_min: # в случае если сгенерировано 1 число (при другом random) , иначе elif 
		counter_min = source_list[i]
		index_min = i
	i += 1 

source_list[index_max], source_list[index_min] = source_list[index_min], source_list[index_max]

print(source_list)
