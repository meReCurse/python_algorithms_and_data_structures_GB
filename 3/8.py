# -*- coding: utf-8 -*-

'''
8. Матрица 5x4 заполняется вводом с клавиатуры кроме
последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю
ячейку строки. В конце следует вывести полученную матрицу.
'''

matrix = [[0] * 4 for x in [0] * 5]
for row in range(len(matrix)):
	row_sum = 0
	print(f'Данные для ввода в строку {row}:')
	for cell in range(len(matrix[row])):
		if cell < len(matrix[row]) - 1:
			print(f'\tДанные для ввода в ячейку {cell}:')
			matrix[row][cell] = int(input('=> '))
			row_sum += matrix[row][cell]
			continue
		matrix[row][cell] = row_sum

for row in matrix:
	string = ''
	for cell in row:
		string += str(cell) + ' '	
	print('\n{:<3}'.format(string))
