# -*- coding: utf-8 -*-

'''
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

from random import random

# заполняем матрицу
matrix = [[0] * 5 for x in [0] * 5]
for row in matrix:
	idx = 0
	for cell in row:
		row[idx] = int(random() * 100) 
		idx += 1

for row in matrix:
	string = '\n'
	for cell in row:
		string += '{:^6}'.format(cell)
	print(string)

i = 0
j = 0
min_num_in_cell = float('inf')
max_of_inferior = float('-inf')
while j < len(matrix[i]):
	while i < len(matrix):
		if matrix[i][j] < min_num_in_cell:
			min_num_in_cell = matrix[i][j]
		i += 1
	if max_of_inferior < min_num_in_cell:
		max_of_inferior = min_num_in_cell

	min_num_in_cell = float('inf')
	i = 0
	j += 1

print('\n{:^6}'.format(max_of_inferior))
