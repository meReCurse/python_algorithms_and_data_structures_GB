# -*- coding: utf-8 -*-

'''
Задача:
7. Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
'''


def match_equal(n):
	result = 0
	for digit in range(1, n + 1):
		result += digit
	if result == n * (n + 1) / 2:
		print('Равенство выполняется.')
	else:
		print('nope')


match_equal(100)


def rec_match_equal(n, result=0, step=1):
	result += step
	if step == n:
		if result == n * (n + 1) / 2:
			print('Равенство выполняется.')
		else:
			print('nope')
		return					
	return rec_match_equal(n, result, step + 1)


rec_match_equal(100)
