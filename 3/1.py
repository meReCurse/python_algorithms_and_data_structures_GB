# -*- coding: utf-8 -*-

'''
Задача 1:
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

'''
Если честно, условие я понял двояко:
1. Первый вариант, перефразирую: существуют ли числа, в указанном диапазоне,
кратные всем числам от 2 до 9.
2. Сделать подсчет сколько всего чисел в диапазоне, кратных
тому или иному числу.

Поэтому сделаю реализацию двух условий.
'''

# 1

def my_filter(func, user_set):
	set_of_nums = set()
	min_range = 2
	max_range = 10
	i = 0
	for el in user_set:
		for j in range(min_range, max_range):
			# Если инвертировать условие, то будет осущ. поиск простых чисел, кроме 2
			if not func(el, j):
				break
			elif j == max_range - 1:
				set_of_nums.add(el)
				i += 1
	return set_of_nums
			

n = set(x for x in range(2, 100))
result = my_filter(lambda x, y: True if x % y == 0 else False, n)
print(result) # таких чисел нет

# 2

list_of_multiples = [0] * 8
for i in range(2, 100):
	for j in range(2, 10):
		if i % j == 0:
			list_of_multiples[j - 2] += 1

i = 0
while i < len(list_of_multiples):
	print(f'{i + 2} - {list_of_multiples[i]}')
	i += 1 
