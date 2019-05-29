# -*- coding: utf-8 -*-

'''
Задача 1:
Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''

import timeit

def reverse_sort(number):
	number = str(number)
	reverse_number = ''
	for i in range(len(number)):
		reverse_number += number[len(number) - 1 - i] 
	return int(reverse_number)


def req_reverse_sort(number):
	number = str(number)
	length = len(number) - 1
	if len(number) == 1:
		return number[length]
	return int(number[length] + str(req_reverse_sort(number[:length])))

''' 
В обоих алгоритмах имеется следующая зависимость от длины передаваемого числа:
При двухзначном числе: 
	reverse_sort() - 0.5
	req_reverse_sort() - 0.582
При трехначном числе:
	reverse_sort() - 0.586
	req_reverse_sort() - 0.991

Полагаю, что имеется линейная зависимость, однако алгоритм с рекурсией
отрабатывает медленнее, в виду наличия преобразования типов на каждом шаге рекурсии и
лишних вычеслений.
Оптимизируем вычисления и преобразования:
'''

def req_reverse_sort(number):
	number = str(number)
	length = len(number) - 1
	if length == 1:
		return number[length]
	return number[length] + req_reverse_sort(number[:length])

'''
При трехначном числе:
	reverse_sort() - 0.670
	req_reverse_sort() - 0.663
Скорость выполнения уменьшилась, при этом заметно, что при некоторых
небольших значениях данных, алгоритм с рекурсией отрабатывает быстрее.
Однако, вышеуказанный алгоритм плох преобразованием данных.
Изменим алгоритм.
'''

def req_reverse_sort(number, length=None):
	if not length:
		length = 10 ** (len(str(number)) - 1)	
	elif length // 10 == 0: 
		return number
	return number % 10 * length + req_reverse_sort(number // 10, length // 10)	

'''
Данная реализация не изменяет тип данных и сокращает время выполнения алгоритма.
При девятизначном числе:
1.65 против второй реализации (1.79) и третьей (3.56).
Однако, даже близко не догоняет при том неоптимизированную итерацию (1.08).
Драма, необходимо посмотреть время выполнения в функциональных языках или
оптимизировать хвостовую рекурсию.
'''

result_1 = timeit.timeit("reverse_sort(123456789)", setup="from __main__ import reverse_sort", number=100000)
result_2 = timeit.timeit("req_reverse_sort(123456789)", setup="from __main__ import req_reverse_sort", number=100000)

print(req_reverse_sort(123456789))
print(f'reverse_sort() - {result_1}')
print(f'req_reverse_sort() - {result_2}')
