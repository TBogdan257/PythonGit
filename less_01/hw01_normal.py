# ------------------------------
# Lessons 01
# __autor__ - Турчин Богдан П.
#-------------------------------
print("*---------------------------*")
print("*  Первое домашнее задание  *")
print("*      hw01_normal.py       *")
print("*       - Задача 1 -        *")
print("*---------------------------*")

x = 58375
y = 2691486
max_digit_x = 0
max_digit_y = 0

print()
print('Решение с помощью цикла while;')

print('Максимальная цифра в числе ', x, end = '')
while x % 10 > 1:
    digit = x % 10
    x //= 10
    if digit > max_digit_x:
        max_digit_x = digit
print('  - ', max_digit_x)
print('---------------------------------')
print()

print('Решение с помощью цикла for;')
print('Максимальная цифра в числе ', y, end = '')
for i in str(y):
    digit = y % 10
    y //= 10
    if digit > max_digit_y:
        max_digit_y = digit
print('  - ', max_digit_y)

print()
print("*---------------------------*")
print("*  Первое домашнее задание  *")
print("*      hw01_normal.py       *")
print("*       - Задача 2 -        *")
print("*---------------------------*")

print("Замена значения переменных местами, используя только две переменные!")

a = input('Введите первое число a = ')
b = input('Введите второе число b = ')

print("Начальное значение переменных a и b >")
print("a = ", a, ";" " b = ", b)

a, b = b, a

print("Конечное значение переменных a и b >")
print("a = ", a, ";" " b = ", b)