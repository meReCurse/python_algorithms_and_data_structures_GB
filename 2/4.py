# -*- coding: utf-8 -*-

'''
Задача:
4. Найти сумму n элементов следующего ряда чисел: 
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
'''


def sum_of_dividing_by_two_sequence(quantity_of_el):
	num = 1
	sum_of_els = 0
	for i in range(quantity_of_el):
		if i % 2 == 0:
			sum_of_els += num
		else:
			sum_of_els -= num
		num /= 2
	print(sum_of_els)


def req_sum_of_dividing_by_two_sequence(quantity_of_el, num=1, step=0):
	if quantity_of_el == 0:
		return 0
	elif step % 2 != 0:
		num = -num
	else:
		num = abs(num)
	return num + req_sum_of_dividing_by_two_sequence(quantity_of_el - 1, num / 2, step + 1)


n = input('Введите длину последовательности: ')

try:
	n = int(n)
except ValueError:
	print('Неверная длина последовательности.')

sum_of_dividing_by_two_sequence(n)
#print(req_sum_of_dividing_by_two_sequence(n))