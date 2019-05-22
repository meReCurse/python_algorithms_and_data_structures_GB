# -*- coding: utf-8 -*-

'''
Задача:
3. Сформировать из введенного числа обратное по порядку
входящих в него цифр и вывести на экран. Например, если
введено число 3486, то надо вывести число 6843.
'''


def reverse_sort(number):
	number = str(number)
	reverse_number = ''
	for i in range(len(number)):
		reverse_number += number[len(number) - 1 - i] 
	return int(reverse_number)


print(reverse_sort(1234))


def req_reverse_sort(number):
	number = str(number)
	length = len(number) - 1
	reverse_number = ''
	if len(number) == 1:
		return number[length]
	reverse_number = number[length]
	number = number[:length]
	return int(reverse_number + str(req_reverse_sort(number)))


print(req_reverse_sort(1234))
