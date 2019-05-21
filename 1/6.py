# -*- coding: utf-8 -*-

'''
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''

position_of_letter = input('Введите позицию буквы в алфавите: ')

try:
    position_of_letter = int(position_of_letter)
    if 1 <= position_of_letter <= 26:
        print(chr(position_of_letter + 96))
    else:
        raise NameError
except (NameError, ValueError):
    print('Неверная позиция')
