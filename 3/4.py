# -*- coding: utf-8 -*-

'''
4. Определить, какое число в массиве встречается чаще всего.
'''

from random import random

# Хоть в условиях не указано не использовать словари, но исходя из названия темы полагаю, что не стоит

source_list = [0] * (int(random() * (100 - 50) + 50)) 
source_list = [int(random() * 2) for x in source_list]

max_repeats = 0
num = 0
for i in range(len(source_list)):
	this_el_repeats = 1
	for j in range(i + 1, len(source_list)):
		if source_list[i] == source_list[j]:
			this_el_repeats += 1;
	if this_el_repeats > max_repeats:
		max_repeats, num = this_el_repeats, source_list[i]

if max_repeats > 1:
	print(f'{source_list}\n{num} - {max_repeats} раз/раза.')
else:
	print(f'Нет повторяющихся элементов.')
