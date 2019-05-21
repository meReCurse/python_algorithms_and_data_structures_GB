# -*- coding: utf-8 -*-

'''
9. Вводятся три разных числа. Найти, какое из них является средним 
(больше одного, но меньше другого).
'''

x = float(input('первое число: '))
y = float(input('второе число: '))
z = float(input('третье число: '))

num = x if x > y else y
num = num if num > z else z

num = int(num) if num == int(num) else num 
print(f'наибольшее число: {num}')
