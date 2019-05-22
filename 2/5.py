# -*- coding: utf-8 -*-

'''
Задача:
5. Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м
включительно. Вывод выполнить в табличной форме:
по десять пар "код-символ" в каждой строке.
'''

ASCII_MIN_RANGE = 32
ASCII_MAX_RANGE = 127


def ASCII_table(min, max):
	symbol = None
	code = None
	string = ''

	for i in range(ASCII_MIN_RANGE, ASCII_MAX_RANGE + 1):
		symbol = chr(i)
		code = ord(symbol)
		string += '{:^3}{:^3} '.format(code, symbol)

		if (i - 1) % 10 == 0:
			print(string)
			string = ''
		elif i == ASCII_MAX_RANGE:
			print(string)		


#ASCII_table(ASCII_MIN_RANGE, ASCII_MAX_RANGE)


def rec_ASCII_table(string='', step=0):
	ASCII_MIN_RANGE = 32
	ASCII_MAX_RANGE = 127	
	symbol = chr(ASCII_MIN_RANGE + step)
	code = ord(symbol)
	string += '{:^3}{:^3} '.format(code, symbol)

	if step == ASCII_MAX_RANGE - ASCII_MIN_RANGE:
		print(string)
		return
	elif (step + 1) % 10 == 0:
		print(string)
		string = ''

	return rec_ASCII_table(string, step + 1)

rec_ASCII_table()
