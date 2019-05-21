# -*- coding: utf-8 -*-

'''
5. Пользователь вводит две буквы. 
Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
'''

def get_position(x):
    return ord(x) - 96

first_letter = input('первая буква: ')
second_letter = input('вторая буква: ')

first_letter_pos = get_position(first_letter)
second_letter_pos = get_position(second_letter)

if first_letter_pos < second_letter_pos:
	between_quantity = second_letter_pos - first_letter_pos - 1	
else:
	between_quantity = first_letter_pos - second_letter_pos - 1

print(f'позиция буквы {first_letter} - {first_letter_pos}')
print(f'позиция буквы {second_letter} - {second_letter_pos}')
print(f'между ними символов - {between_quantity}')
