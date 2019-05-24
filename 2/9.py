# -*- coding: utf-8 -*-

'''
Задача:
9. Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
'''

from random import random


def num_with_max_sum(quantity):
	max_sum_of_nums = 0
	cached_num = 0
	for i in range(quantity + 1):
		number = input('Введите натуральное число: ')
		sum_of_one_num = 0
		for digit in number:
			sum_of_one_num += int(digit)
		if sum_of_one_num > max_sum_of_nums:
			max_sum_of_nums = sum_of_one_num
			cached_num = number
		elif max_sum_of_nums == sum_of_one_num:
			cached_num += ' ' + number
	print(f'Наибольшее по сумме число/числа {cached_num}, сумма цифр составляет {max_sum_of_nums}')


#quantity_of_nums = int(random() * (4 - 2) + 2)
#num_with_max_sum(quantity_of_nums)


def kant_would_be_proud_thing_in_itself_ultimate_function():
	quantity_of_nums = int(random() * (4 - 2) + 2)
	max_sum_of_digits = 0
	max_number = 0

	def count_quantity(step=1):
		nonlocal max_sum_of_digits
		nonlocal max_number
		nonlocal quantity_of_nums

		if step > quantity_of_nums:
			return 0
		number = int(input('Введите натуральное число: '))

		def count_sum(number):
			if number == 0:
				return 0
			return number % 10 + count_sum(number // 10)

		sum_of_one_num = count_sum(number)
		if max_sum_of_digits < sum_of_one_num:
			max_sum_of_digits = sum_of_one_num
			max_number = number 
		elif max_sum_of_digits == sum_of_one_num:
			max_number = str(max_number) + ' ' + str(number)

		return count_quantity(step + 1)

	count_quantity()
	print(f'Наибольшее по сумме число/числа {max_number}, сумма цифр составляет {max_sum_of_digits}')


kant_would_be_proud_thing_in_itself_ultimate_function()
