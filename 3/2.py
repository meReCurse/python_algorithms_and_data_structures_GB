# -*- coding: utf-8 -*-

'''
2. Во втором массиве сохранить индексы
четных элементов первого массива. Например,
если дан массив со значениями 8, 3, 15, 6, 4, 2,
то во второй массив надо заполнить значениями
1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
'''

from random import random

# Создадим массив по условию (со случайными позициями чисел)
source_list = [x for x in range(0, 21)]
i = 0
while i < len(source_list):
	rand_index = int(random() * 21)
	source_list[rand_index], source_list[i] = source_list[i], source_list[rand_index]
	i += 1

object_list = [source_list.index(x) for x in source_list if x % 2 == 0]
print(f'В исходном списке:\n{source_list},\nпозиции четных элементов:\n{object_list}')

# без использования метода index:
object_list = []
i = 0
for num in source_list:
	if num % 2 == 0:
		object_list.append(i)
	i += 1
print(object_list)
