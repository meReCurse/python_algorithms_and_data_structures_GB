# -*- coding: utf-8 -*-

'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это
цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

# решение списком
num1 = [x for x in input('Введите 1-е hex число: ')]
num2 = [x for x in input('Введите 2-е hex число: ')]
add = hex(int('0x' + ''.join(num1), 16) + int('0x' + ''.join(num2), 16))
compose =  hex(int('0x' + ''.join(num1), 16) * int('0x' + ''.join(num2), 16))
result1 = [x.upper() for x in add[2:]]
result2 = [x.upper() for x in compose[2:]]
print(result1)
print(result2)

# решение на классах
class HexCalc:
    def __init__(self, num1, num2):
        self.num1 = [x for x in num1]
        self.num2 = [x for x in num2]
        self.__hex_converter__()
    def __hex_converter__(self):
        self.hex_num1 = int('0x'+ ''.join(self.num1), 16)
        self.hex_num2 = int('0x'+ ''.join(self.num2), 16)
    def __result_converter__(self, result):
        return [x.upper() for x in hex(result)[2:]]
    def add(self):
        result = self.hex_num1 + self.hex_num2
        return self.__result_converter__(result)
    def compose(self):
        result = self.hex_num1 * self.hex_num2
        return self.__result_converter__(result)
# немного переделал начальный алгоритм, чтобы было меньше повторений преобразований
calc = HexCalc('A2', 'C4F')
print(calc.add())
print(calc.compose())

# решение коллекцией
import collections

Nums = collections.namedtuple('Nums', ['num1', 'num2'])
nums = Nums([x for x in input('1-е hex число: ')], [x for x in input('2-е hex число: ')])
add = hex(int('0x' + ''.join(nums.num1), 16) + int('0x' + ''.join(nums.num2), 16))
compose =  hex(int('0x' + ''.join(nums.num1), 16) * int('0x' + ''.join(nums.num2), 16))
result1 = [x.upper() for x in add[2:]]
result2 = [x.upper() for x in compose[2:]]
print(result1)
print(result2)
