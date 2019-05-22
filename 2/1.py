# -*- coding: utf-8 -*-

'''
Задача:
Написать программу, которая будет складывать, вычитать, 
умножать или делить два числа. Числа и знак операции вводятся 
пользователем. После выполнения вычисления программа не должна 
завершаться, а должна запрашивать новые данные для вычислений. 
Завершение программы должно выполняться при вводе символа '0' 
в качестве знака операции. Если пользователь вводит неверный знак 
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
и снова запрашивать знак операции. Также сообщать пользователю о невозможности
деления на ноль, если он ввел 0 в качестве делителя.
'''


def calc():
	while True:
		try:
			operand_one = float(input('Введите число 1: '))
			operand_two = float(input('Введите число 2: '))
		except ValueError:
			print("Недопустимый операнд." )
			continue

		operator = input('Введите операнд (0, +, -, *, /): ')

		if operator == '0':
			print('Выход из программы.')
			break
		elif operator == '+':
			print(operand_one + operand_two)
		elif operator == '-':
			print(operand_one - operand_two)
		elif operator == '*':
			print(operand_one * operand_two)
		elif operator == '/':
			if operand_two > 0:
				print(operand_one / operand_two)
			else:
				print("Деление на ноль недопустимо.")	
		else:
			print("Неверный оператор.")


calc()


def rec_calc(operator = 1):
	try:
		operand_one = float(input('Введите число 1: '))
		operand_two = float(input('Введите число 2: '))
	except ValueError:
		print("Недопустимый операнд." )
		rec_calc()

	operator = input('Введите операнд (0, +, -, *, /): ')

	if operator == '0':
		print('Выход из программы.')
		return
	elif operator == '+':
		print(operand_one + operand_two)
	elif operator == '-':
		print(operand_one - operand_two)
	elif operator == '*':
		print(operand_one * operand_two)
	elif operator == '/':
		if operand_two > 0:
			print(operand_one / operand_two)
		else:
			print("Деление на ноль недопустимо.")	
	else:
		print("Неверный оператор.")	

	rec_calc(operator)


#rec_calc()