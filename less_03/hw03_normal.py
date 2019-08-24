# ------------------------------
# Lessons 03
# __autor__ - Турчин Богдан П.
#-------------------------------
import math
import datetime
import random

print("*-------------------------------*")
print("*    Второе домашнее задание    *")
print("*        hw03_normal.py         *")
print("*           Задача 1            *")
print("*-------------------------------*")

def fibonacci(n, m):
    fib1 = fib2 = 1
    if m <= n:
        print('Не верный диапазон!')
        return ''
    if n < 2 and m > n:
        print(fib1, end=' ')
        print(fib2, end=' ')
        k = 2
    elif n == 2:
        print(fib2, end=' ')
        k = n
    elif n == 2:
        k = n
    elif n > 2:
        for i in range(3, n):
            fib1, fib2 = fib2, fib1 + fib2
        k = n - 1
    for i in range(k, m):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

print('Введите диапазон вывда чисел Фибоначи: \n ')
x = int(input('Введите начальное число диапазона х = '))
y = int(input('Введите конечное  число диапазона y = '))

fibonacci(x, y)
print()
print()

print("*-------------------------------*")
print("*    Второе домашнее задание    *")
print("*        hw03_normal.py         *")
print("*           Задача 2            *")
print("*-------------------------------*")
print("*---------------------------------------------------------------------------------*")
print('* Напишите функцию, сортирующую принимаемый список по возрастанию.                *')
print('* Для сортировки используйте любой алгоритм (например, пузырьковый).              *')
print('* Для решения данной задачи нельзя использовать встроенную функцию и метод sort() *')
print("*---------------------------------------------------------------------------------*")

list_num = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print('--------  Исходный список  --------')
print(list_num)
print('-----------------------------------')
print()

print('---- Первый способ - цикл for  ----')
def sort_to_max_my(in_list):
    N = len(in_list)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if in_list[j] > in_list[j + 1]:
                in_list[j], in_list[j + 1] = in_list[j + 1], in_list[j]
    return in_list

print(sort_to_max_my(list_num))

print('---- Второй способ - цикл while ---')
list_num = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print(list_num)

def sort_to_max_whil(in_list):
    i =0
    N = len(in_list)
    while i < N - 1:
        j = 0
        while j < N - 1 - i:
            if in_list[j] > in_list[j + 1]:
                in_list[j], in_list[j + 1] = in_list[j + 1], in_list[j]
            j += 1
        i += 1
    return in_list
print(sort_to_max_whil(list_num))

print('--------  Метод пузырков   --------')
list_num = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print(list_num)

def bubble_sort(in_list):
    N = len(in_list)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if in_list[j] > in_list[j + 1]:
                buff = in_list[j]
                in_list[j] = in_list[j + 1]
                in_list[j + 1] = buff
    return in_list

print(bubble_sort(list_num))

print('---------  Функция sorted ---------')
list_num = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print(list_num)

def sort_to_max_mine(origin_list):
    return sorted(origin_list)

print(sort_to_max_mine(list_num))

print('--------------------------------------------')
print('Как видно результат всех функций одинаковый!')
print('--------------------------------------------')
print()

print("*-------------------------------*")
print("*    Второе домашнее задание    *")
print("*        hw03_normal.py         *")
print("*           Задача 3            *")
print("*-------------------------------*")
#print()
print("*-------------------------------------------------------------*")
print('* Напишите собственную реализацию стандартной функции filter. *')
print('* Разумеется, внутри нельзя использовать саму функцию filter. *')
print("*-------------------------------------------------------------*")
print('Дансписок цветов. Необходимо отфильтровать по цветку "Роза".')

flowers = ['Тюльпан', 'Роза', 'Георгина', 'Лютик', 'Роза', 'Лилия', 'Ирис', 'Роза', 'Нарцисс', 'Лютик']
print(flowers)
print()

def flow_sort(in_var, sort_name):
    out = []
    for i in range(0, len(flowers)):
        if in_var[i] == sort_name:
            out.append(in_var[i])
    return out

flower_sort = input('Введите название цветка, по которому хотите сортировать: ')
print('Отфильтрованный список:')
print(flow_sort(flowers, flower_sort))