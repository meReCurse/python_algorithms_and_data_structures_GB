# -*- coding: utf-8 -*-

'''
Задача:
2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, то у него 3 
четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''


def odd_and_even_quantity(natural_number):
	even = 0
	odd = 0
	for digit in natural_number:
		if int(digit) % 2 == 0:
			even += 1
		else:
			odd += 1
	print(f'Количество четных цифр в числе: {even}')
	print(f'Количество нечетных цифр в числе: {odd}')


#odd_and_even_quantity(input('Введите число: '))


def rec_odd_and_even_quantity(natural_number, even=0, odd=0, rec_step=0):
	if natural_number == 0 and rec_step > 0:
		print(f'Количество четных цифр в числе: {even}')
		print(f'Количество нечетных цифр в числе: {odd}')
		return
	last_digit = natural_number % 10 
	natural_number = natural_number // 10

	if last_digit % 2 == 0:
		even += 1
	else:
		odd += 1
		
	rec_step += 1
	rec_odd_and_even_quantity(natural_number, even, odd, rec_step)


rec_odd_and_even_quantity(int(input('Введите число: ')))
