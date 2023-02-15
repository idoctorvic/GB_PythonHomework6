""" Определить индексы элементов массива (списка), значения которых 
принадлежат заданному диапазону (т.е. не меньше заданного минимума и 
не больше заданного максимума) """

from random import randint

def index_list(n, min_border, max_border):
    ind_list = []
    for i in range(n):
        if min_border <= a[i] <= max_border:
            ind_list.append(i)
    return ind_list

n = int(input('Enter the length of massive: '))
min_border = int(input('Enter the minimum number: '))
max_border = int(input('Enter the maximium number: '))
a = [randint(-10, 10) for i in range(n)]

print(a)
print(index_list(n, min_border, max_border))