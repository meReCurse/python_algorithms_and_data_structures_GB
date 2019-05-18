# -*- coding: utf-8 -*-

'''
4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
'''

from random import random

# случайное целое число
max_num = int(input('Максимальная граница: '))
min_num = int(input('Минимальная граница: '))
random_num = int(random() * (max_num - min_num + 1)) + min_num
print(random_num)

# случайное вещественное число
max_num = float(input('Максимальная граница: '))
min_num = float(input('Минимальная граница: '))
random_num = random() * (max_num - min_num) + min_num
print(round(random_num, 5))

# случайный символ
max_chr = ord(input('Максимальная граница: '))
min_chr = ord(input('Минимальная граница: '))
random_ascii = int(random() * (max_chr - min_chr + 1)) + min_chr
print(chr(random_ascii))
