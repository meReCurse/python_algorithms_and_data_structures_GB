# -*- coding: utf-8 -*-

'''
Задача:
8. Посчитать, сколько раз встречается определенная цифра
в введенной последовательности чисел. Количество вводимых
чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''


def find_digit_quantity(n, d):
	i = 0
	for digit in n:
		if digit == str(d):
			i += 1
	print(f'В чиcле {n} цифра {d}, встречается {i} раз/раза.')


def rec_find_digit(n, d, result=0):
	if len(n) == 0:
		print(f'Цифра {d}, встречается {result} раз/раза.')
		return
	elif n[len(n) - 1] == d:
		result += 1 
	n = n[:len(n) - 1]
	rec_find_digit(n, d, result)


number = input('Введите число: ')
digit = input('Цифра, встречающаяся в числе:')

if 0 <= int(digit) < 10: 
	#find_digit_quantity(number, digit)
	rec_find_digit(number, digit)
else:
	print('Такой цифры нет.')
