# -*- coding: utf-8 -*-

'''
Задача:
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

x = input('Введите трехзначное число: ')
try:
    x = int(x)
    if 100 <= x < 1000:
        first_number = x % 10
        second_number = x // 10 % 10
        third_number = x // 100 % 10 
        sum_of_nums = first_number + second_number + third_number
        product_of_nums = first_number * second_number * third_number
        print(f'Сумма чисел = {sum_of_nums}')
        print(f'Произведение чисел = {product_of_nums}') 
    else:
        raise ValueError
except ValueError:
    print ('Указан неверный формат числа') 
