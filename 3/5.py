# -*- coding: utf-8 -*-

'''
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
'''

from random import random


source_list = [0] * (int(random() * 26))
source_list = [round(float(random() * (100 + 100) - 100), 2) for x in source_list]

max_neg_num = float('-inf')
index = 0
source_list = list(set(source_list))
print(source_list)

for i in range(len(source_list)):
	if source_list[i] < 0 and source_list[i] > max_neg_num:
		max_neg_num = source_list[i]
		index = i

if max_neg_num > float('-inf'): # если массив не пуст
	print(f'максимальное отрицательное число: {max_neg_num}\nего индекс: {index}')
else:
	print(f'сгенерированы только положительные числа.')
