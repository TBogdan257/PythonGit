# ------------------------------
# Lessons 02
# __autor__ - Турчин Богдан П.
#-------------------------------
import math
import datetime
import random

print("*---------------------------*")
print("*  Второе домашнее задание  *")
print("*      hw02_normal.py       *")
print("*         Задача 1          *")
print("*---------------------------*")

list_number = [3, 1, -5, 36, 72, 4, -3, 9, 25, 49, -1, 16, 64]
list_number_new = []

for rez in list_number:
    if rez > 0:
        if math.sqrt(rez) % 1 == 0:
            list_number_new.append(math.sqrt(rez))

print(list_number_new)
print()

print("*---------------------------*")
print("*  Второе домашнее задание  *")
print("*      hw02_normal.py       *")
print("*         Задача 2          *")
print("*---------------------------*")

from datetime import date
import locale
locale.setlocale(locale.LC_ALL, "")

today = date.today()
day = ['','Первое', 'Второе', 'Третье', 'Четвертое', 'Пятое', 'Шестое', 'Седьмое',
       'Восьмое', 'Девятое', 'Десятое', 'Одиннадцатое', 'Двенадцатое', 'Тринадцатое ',
       'Четырнадцатое', 'Пятнадцатое', 'Шестнадцатое', 'Семнадцатое', 'Восемнадцатое',
       'Девятнадцатое', 'Двадцатое', 'Двадцать первое', 'Двадцать второе', 'Двадцать третье',
       'Двадцать четвертое', 'Двадцать пятое', 'Двадцать шестое', 'Двадцать седьмое',
       'Двадцать восьмое', 'Двадцать девятое', 'Тридцатое', 'Тридцать первое']

month = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа',
         'сентября', 'октября', 'ноября', 'декабря']

print(today)
str_day = day[today.day]
str_month = month[today.month]

print("{} {} {} года".format(str_day, str_month, today.year))
print(today.strftime("%d %B %Y (%A)"))
print('---------------------')
print()

print("*---------------------------*")
print("*  Второе домашнее задание  *")
print("*      hw02_normal.py       *")
print("*         Задача 3          *")
print("*---------------------------*")

n = int(input('Введите количество элементов n: '))

list_rnd = []

for i in range(0, n):
    list_rnd.append(random.randint(-100, 100))

print(list_rnd)

for i in range(0, (n + 1) * 4):
    print('-', end='')
print()

print("*---------------------------*")
print("*  Второе домашнее задание  *")
print("*      hw02_normal.py       *")
print("*         Задача 4а         *")
print("*---------------------------*")

from itertools import groupby

#           0  1  2   3   4  5  6  7   8   9 10  11  12  13
list_num = [3, 1, 5, 36, 72, 4, 3, 9, 25, 49, 1, 16, 64, 72]
list_num2 = []
dubl = 0

print()
print('Первый способ удаления повторяющихся элементов списка: ')
print(list(set(list_num)))
print('---------------------------------------')
print()
print('Второй способ удаления повторяющихся элементов списка: ')
def fun(list_num):
    n = []
    for i in list_num:
        if i not in n:
            n.append(i)
    return n

print(fun(list_num))
print('---------------------------------------')

print('Ещё один способ удаления повторяющихся элементов списка: ')
for inum in range(0, len(list_num) - 1 - dubl):
    bool_var = True
    #print(len(list_num) - 1)
    for jnum in range(inum + 1, len(list_num)):
        if list_num[inum] != list_num[jnum]:
            continue
        else:
            list_num.pop(jnum)
            bool_var = False
            dubl += 1
            break
    if bool_var:
        pass
        #list_num2.append(list_num[inum]) # Не пойму, почему здесь индекс выходит за пределы диаппазона?

#print(list_num2)
print('Не пойму, почему здесь индекс выходит за пределы диаппазона?')

print("*---------------------------*")
print("*  Второе домашнее задание  *")
print("*      hw02_normal.py       *")
print("*         Задача 4б         *")
print("*---------------------------*")

list_num1 = [13, 2, 5, 33, 8, 3, 2, 45, 33, 8, 11]

print(list_num1, ' - Исходный список')

def fun_rep(list_n):
    new = []
    for k in list_n:
        if (k) not in new:
            new.append(k)
        else:
            new.remove(k)

    return new

print(fun_rep(list_num1), '                     - Очищенный список!')