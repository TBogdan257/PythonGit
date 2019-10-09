# Урок 2. Задание № 6
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или
# меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.
# ---------------------------------------------------------
# Задание выполнил студент GeekBrains  Турчин Богдан.
# ---------------------------------------------------------
import random

# Загадываем случайное число
num_rnd = random.randint(0, 100)

# Определяем количество попыток
n = 10
for i in range(1, n + 1):
    num = int(input(f'{i}. Введите число '))
    if num == num_rnd:
        print('Поздравляю! Вы угадали число  :)')
        break
    elif num < num_rnd and i < n:
        print('Задуманное число больше введенного  :(')
    elif num > num_rnd and i < n:
        print('Задуманное число меньше введенного  :(')
    else:
        print('---------------------------------------------')
        print(f'За 10 попыток Вы не угадали загаданное число.\nОно равно {num_rnd}')
