# -*- coding: utf-8 -*-

'''
Задача:
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше
введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.
'''

from random import random


CHANCES = 10


def guess_number(chances):	
	random_num = int(random() * (101))
	while chances != 0:
		user_number = int(input('Введите число: '))
		if user_number > random_num:
			print('Введенное число больше.')
		elif user_number < random_num:
			print('Введенное число меньше.')
		else:
			print('Вы угадали.')
			break
		chances -= 1
		if chances == 0:
			print(f'Попытки закончились. Загадано {random_num}')


#guess_number(CHANCES):


def rec_guess_number():
	random_num = int(random() * (101))
	chances = 10
	def game(chances, random_num=random_num):
		if chances == 0:
			print(f'Попытки закончились. Загадано {random_num}')
			return
		user_number = int(input('Введите число: '))
		if user_number == random_num:
			print('Вы угадали')
			return
		elif user_number > random_num:
			print('Введенное число больше.')
		elif user_number < random_num:
			print('Введенное число меньше.')
		game(chances - 1)
	game(chances)


rec_guess_number()
