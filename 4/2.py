# -*- coding: utf-8 -*-

'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию:
Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
'''

import timeit

N = 20

def i_prime(n):
	check_number = 1
	while n > 0:
		check_number += 1
		if check_number != 2 and check_number % 2 == 0:
			continue
		divider = 2
		is_prime = True
		while divider * divider <= check_number:
			if check_number % divider == 0:
				is_prime = False
				break
			divider += 1
		if is_prime:
			n -= 1
	return check_number

# Исходя из того, что в задании не говорится о генерации некоего диапазона
# сделал реализацию без указания этого диапазона, соответственно решето
# проверяет каждый вновь добавленный элемент по правилам решета 
def ert_i_prime(n):
	list_of_nums = [0] * 2
	copy = []
	candidate = 2
	while len(copy) <= n:
		list_of_nums.append(candidate)

		divider = 2
		while divider < len(list_of_nums):
			if list_of_nums[divider] != 0:
				next_num_idx = divider * 2
				while next_num_idx < len(list_of_nums):
					list_of_nums[next_num_idx] = 0
					next_num_idx += divider
			divider += 1

		for num in list_of_nums:
			if num not in copy:
				copy.append(num)
		candidate += 1
	return copy.pop()

print(i_prime(2))
print(ert_i_prime(2))

print(timeit.timeit('i_prime(N)', setup='from __main__ import i_prime, N', number=100))
#сложность O(N) 1.619296503 при N = 100 ; 4.804297475 при N = 200
print(timeit.timeit('ert_i_prime(N)', setup='from __main__ import ert_i_prime, N', number=100))
'''
36.89 при N = 100. 
при решении задачи с заранее неизвестным диапазоном
скорость второго алгоритма ниже, в виду наличия дополнительных циклов. Очевидно,
что скорость выполнения будет быстрее при заранее указанном диапазоне.
В данной реализации сложность получилась возможно O(N*N)
'''
