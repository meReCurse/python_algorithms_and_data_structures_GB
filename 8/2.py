# -*- coding: utf-8 -*-

'''
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
### дополнительно: использовать Collections
'''

from collections import Counter, OrderedDict


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def get_child(self):
        return self.left, self.right


def haffman_tree(string):
    count_el = Counter(string)
    sorted_dict= OrderedDict(
        sorted(
            count_el.items(), 
            reverse=True, 
            key=lambda x: x[1]
            )
        )
    while True:
        left = sorted_dict.popitem()
        right = sorted_dict.popitem()
        freq = left[1] + right[1]
        node = Node(left[0], right[0])
        sorted_dict[node] = freq
        sorted_dict = OrderedDict(
            sorted(
                sorted_dict.items(),
                reverse=True,
                key=lambda x: x[1]
                )
            )
        if len(sorted_dict) == 1:
            break
        
    return sorted_dict

def haffman_code(node, code=''):
    if isinstance(node, str):
        return {
            node: code    
        }

    l, r = node.left, node.right
    result = {}

    result.update(haffman_code(l, f'{code}0'))
    result.update(haffman_code(r, f'{code}1'))

    return result

string = 'spam eggs ham'
tree = haffman_tree(string)
table_of_codes = None
for el in tree:
     table_of_codes = haffman_code(el)

codded_str = ''

for char in string:
    codded_str += table_of_codes[char]

print(f'{string} - {codded_str}')