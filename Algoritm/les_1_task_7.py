# Урок 1. Задание № 7
# По данным трех отрезков, введенныз пользователем, определить
# возможность существования треугольника , составленного из этих
# отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.
# ---------------------------------------------------------
# Задание выполнил студент GeekBrains  Турчин Богдан.
# ---------------------------------------------------------
a = float(input('Введите длину стороны тругольника a = '))
b = float(input('Введите длину стороны тругольника b = '))
c = float(input('Введите длину стороны тругольника c = '))

if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):
    print('Треугольник не существует!')

elif (a == b) and (a == c):
    print('Тркугольник равносторонний!')

elif ((a == b) and (a != c)) or ((b == c) and (a != b)) or ((a == c) and (a != b)):
    print('Тркугольник равнобедренный!')

else:
    print('Тркугольник является разносторонним!')