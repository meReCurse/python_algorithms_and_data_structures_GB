# -*- coding: utf-8 -*-
 
"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler.asizeof import asizeof

SIZES = [																	
	{'size':'большой', 'price': 100, 'calories': 40},
	{'size':'маленький','price': 50, 'calories': 20}
]
FILLS = [
	{'fill':'сыр', 'price': 10, 'calories': 20},
	{'fill': 'салат', 'price': 20, 'calories': 5},
	{'fill': 'картофель', 'price': 15, 'calories': 10}
]
OPTIONS =[	
	{'option': '-', 'price': 0, 'calories': 0},	
	{'option': 'приправа', 'price': 15, 'calories': 0},
	{'option': 'майонез', 'price': 20, 'calories': 5}
]


class Hamburger:
	__slots__ = 'size', 'fill', 'option', 'price', 'calories'
	def __init__(self):
		self.size = ''
		self.fill = ''
		self.option = ''
		self.price = 0
		self.calories = 0
	def __str__(self):
		return f'Размер: {self.size}\
				\nНаполнитель: {self.fill}\
				\nДополнительно: {self.option}\
				\nЦена: {self.price}\
				\nКалорийность: {self.calories}'

	def set_size(self, size_dict):
		self.size = size_dict['size']
		self.set_price(size_dict['price'])
		self.set_calories(size_dict['calories'])

	def set_fill(self, fill_dict):
		self.fill = fill_dict['fill']
		self.set_price(fill_dict['price'])
		self.set_calories(fill_dict['calories'])

	def set_options(self, option_dict):
		self.option = option_dict['option']
		self.set_price(option_dict['price'])
		self.set_calories(option_dict['calories'])

	def set_price(self, price):
		self.price += price

	def set_calories(self, calories):
		self.calories += calories


class Shop:
	# params {list of dicts}
	__slots__ = 'sizes', 'fills', 'options'
	def __init__(self, sizes, fills, options):
		self.sizes = sizes
		self.fills = fills
		self.options = options

	def order(self):
		hamburger = Hamburger()
		for el in self.__slots__:
			self.change_hamburger(hamburger, getattr(self, el), el[:-1])

		return hamburger

	''' without slots '''
	# def order(self):
	# 	hamburger = Hamburger() 

	# 	for k, v in self.__dict__.items():
	# 		self.change_hamburger(hamburger, v, k[:-1])
	# 	return hamburger

	''' params {dict} variants '''
	def change_hamburger(self, hamburger, variants, key):
		choice = 0
		i = 1
		print('Для выбора укажите цифру: ')
		for variant in variants:
			print(f'{i}.{variant[key]}')
			i += 1
		choice = int(input(': '))
		if key == 'size':
			hamburger.set_size(variants[choice - 1])
		elif key == 'fill':
			hamburger.set_fill(variants[choice - 1])
		else:
			hamburger.set_options(variants[choice - 1])

shop = Shop(SIZES, FILLS, OPTIONS)
hamburger = shop.order()
print(hamburger)
#print(asizeof(hamburger))
#print(asizeof(shop))

'''
class Hamburger:
	Без использования __slots__ аттрибуты экземпляров класса Hamburger занимают 464 B,
	С использованием __slots__ : 240 B.
В данном случае __slots__ позволил сократить занимаемую память почти в 2 раза.
class Shop:
	Без использования __slots__ аттрибуты экземпляров класса Shop занимают 2.135 KiB
	С использованием __slots__ аттрибуты экземпляров класса Shop занимают 1.976 KiB
В данном случае __slots__ позволил сократить занимаемую память на 159 B. Результаты можно
увеличить, если изменить способы хранения данных в константах, список словарей все же
довольно нагруженная конструкция. Изменение на матрицу сократит занимаемую память
почти в два раза (но значительно уменьшит читаемость).
Вообщем по заданиям можно сделать следующие выводы: 
1. в общем случае скорость исполнения пропорциональна занимаемой памяти
2. занимаемая память пропорциональна читаемости
'''