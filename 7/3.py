# -*- coding: utf-8 -*- 

'''
Задание 3: 
Массив размером 2m + 1, где
m – натуральное число, заполнен
случайным образом. Найдите в массиве
медиану. Медианой называется элемент
ряда, делящий его на две равные части:
в одной находятся элементы, которые не
меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод
сортировки, который не рассматривался на уроках
'''

from random import randint, choice


def quickselect_median(li):
	'''
	функция определяет необходимую для 
	поиска медианы позицию в списке и передает
	список и позицию в реализацию алгоритма Хоара (fastselect).
	:param li: list of nums
	:return: вызов функции реализации алгоритма Хоара
	'''
	if len(li) % 2 == 1:
		return hoare_quickselect(li, len(li) // 2)
	else:
		return 0.5 * (
			hoare_quickselect(li, len(li) // 2) +
			hoare_quickselect(li, len(li) // 2 - 1)
			)


def hoare_quickselect(li, i):
	'''
	Функция реализует алгоритм Хоара.
	Не сортируя список вычисляет значение
	по передаваемой позиции, как если бы список был отсортирован.
	:param li: list of nums
	:param i: idx искомого элемента
	:return: int значение искомого элемента.
	'''
	if len(li) == 1:
		return li[0]

	pivot = choice(li)

	lows = [el for el in li if el < pivot]
	highs = [el for el in li if el > pivot]
	pivots = [el for el in li if el == pivot]

	if i < len(lows):
		return hoare_quickselect(lows, i)
	elif i < len(lows) + len(pivots):
		return pivots[0]
	else:
		return hoare_quickselect(highs, i - len(lows) - len(pivots))


# дополнительно:
def cocktail_sort(li):
	'''
	Функция реализует алгоритм шейкерной сортировки.
	:param li: list of nums
	:return: sorted same list (asc)
	'''
	left = 0
	right = len(li) - 1

	while left <= right:
		for i in range(left, right, +1):
			if li[i] > li[i + 1]:
				li[i], li[i + 1] = li[i + 1], li[i]
		right -= 1

		for i in range(right, left, -1):
			if li[i] < li[i - 1]:
				li[i], li[i - 1] = li[i - 1], li[i]
		left += 1

	return li

def shell_sort(li):
	'''
	Функция реализует алгоритм сортировки Шелла.
	:param li: list of nums
	:return: sorted same list (asc)
	'''
	n = len(li)
	gap = n // 2

	while gap > 0:
		for i in range(gap, n):
			temp = li[i]
			j = i

			while j >= gap and li[j - gap] > temp:
				li[j] = li[j - gap]
				j -= gap
			li[j] = temp
			
		gap //= 2
	return li

def find_median(li):
	'''
	Функция ищет медиану в отсортированном списке.
	:param li: list of nums
	:return: int median
	'''
	result = li[len(li) // 2]
	if len(li) % 2 == 1:
		return result
	return 0.5 * (result + li[len(li) // 2 + 1])

n = 2
length = 2 * n + 1
li = [randint(1, 100) for x in range(length)]

print(f'\nсписок: {li}')

median = quickselect_median(li)
print('\nmedian with Hoare:')
print(f'медиана ряда чисел: {median}')

copy = cocktail_sort(li.copy())
median = find_median(copy)
print('\nmedian with coctail:')
print(f'sorted list: {copy}')
print(f'медиана ряда чисел: {median}')

copy = shell_sort(li.copy())
median = find_median(copy)
print('\nmedian with Shell:')
print(f'sorted list: {copy}')
print(f'медиана ряда чисел: {median}')
