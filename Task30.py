#  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_num = int(input("Введите первое число: ")) 
second_num = int(input("Введите шаг: "))
three_num = int(input("Введите количество чисел: "))
for i in range(three_num):
    print(first_num + i * second_num, end=' ')