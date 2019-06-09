# -*- coding: utf-8 -*-

'''
1. Определение количества различных подстрок
с использованием хэш-функции. Пусть дана строка
S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
'''
import hashlib


def sum_of_sub_str(string):
    n = len(string)    
    uniqs = set()
    for i in range(n):
        if i == 0:
            n = len(string) - 1
        else:
            n = len(string)
        for j in range(n, i, -1):
            sub_str = string[i:j]
            if ' ' not in sub_str:
                uniqs.add(hashlib.sha1(sub_str.encode('utf-8')).hexdigest())
    return uniqs

S = 'span span   '
uniqs = sum_of_sub_str(S)
print(f'количество уникальных подстрок в строке "{S}" = {len(uniqs)}')