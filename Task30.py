""" Заполните массив элементами арифметической прогрессии. Её первый 
элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки. """

def ariph_list(beginning, diff, list_length):
    for i in range(1, list_length + 1):
        print(beginning + (i - 1)*diff)

a = int(input('Enter the beginning of the list: '))
b = int(input('Enter the progression difference: '))
c = int(input('Enter the length of the resulting list: '))

ariph_list(a, b, c)