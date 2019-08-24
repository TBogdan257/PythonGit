# ------------------------------
# Lessons 02
# __autor__ - Турчин Богдан П.
#-------------------------------
print("*---------------------------*")
print("*  Второе домашнее задание  *")
print("*       hw02_easy.py        *")
print("*         Задача 1          *")
print("*---------------------------*")

list_fruits = ["яблоко","банан","киви","арбуз"]

print('1.{0}'.format(list_fruits[0]))
print('2. {0}'.format(list_fruits[1]))
print('3.  {0}'.format(list_fruits[2]))
print('4. {0}'.format(list_fruits[3].title()))
print('---------------------------------------------')

print('            Ещё один вариант')

for item in list_fruits:
    print(f'{list_fruits.index(item) + 1}. {item}')

for i in range(0, 45):
    print('-', end='')
print()
print()

print("*---------------------------*")
print("*  Второе домашнее задание  *")
print("*       hw02_easy.py        *")
print("*         Задача 2          *")
print("*---------------------------*")

list_1 = [68, 'one', 23, 'animals', 34, 122, 125, 'too', 155]
list_2 = [15, 68, 235, 155, 78, 23, 125, 34, 'animals']

print('Первый список: ', list_1)
print('Второй список: ', list_2)

for itm1 in list_1:
    for itm2 in list_2:
        if itm1 == itm2:
            print(itm1, itm2)
            list_1.remove(itm2)

print('Результат:', list_1)
print()
print('---------------------------------------------')

print("*---------------------------*")
print("*  Второе домашнее задание  *")
print("*       hw02_easy.py        *")
print("*         Задача 3          *")
print("*---------------------------*")
print()
list_number = [1, 2, 4, 5, 8, 9, 11, 12, 15, 17, 19, 20, 23, 45, 68, 73, 89]
print('Произвольный список из целых чисел:')
print(list_number)
print()
print('Задание:')
print('Если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.')

for num in list_number:
    if num % 2 == 0:
        print(num, ' - ', num, '/ 4 = ', num / 4, ';')
    else:
        print(num, ' - ', num, '* 2 = ', num * 2, ';')

print('---------------------------------------------')

print('Маленький бонус!')
name = 'Иван'
surname = 'Иванов'

print('Добро пожаловать, {0} {1}, на коференцию.'.format(name, surname))