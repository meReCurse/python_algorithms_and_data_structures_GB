# -*- coding: utf-8 -*-

'''
7. В одномерном массиве целых чисел определить два
наименьших элемента. Они могут быть как равны между собой (оба являться минимальными),
так и различаться.
'''

from random import random


source_list = [0] * (int(random() * 15))
source_list = [int(random() * 100) for x in source_list]
print(source_list)

min_num = float('inf')
min_idx = 0
second_min_num = float('inf')
second_min_idx = 0

if len(source_list) > 0:
	for num in source_list:
		if num < min_num:
			min_num = num
			min_idx = source_list.index(num)
	print(f'{min_num} - idx {min_idx}')
else:
	print(f'Сгенерирован пустой массив.')
	
if len(source_list) > 1:
	for num in range(len(source_list)):
		if min_idx != num and source_list[num] < second_min_num:
			second_min_num = source_list[num]
			second_min_idx = num
	print(f'{second_min_num} - idx {second_min_idx}')
