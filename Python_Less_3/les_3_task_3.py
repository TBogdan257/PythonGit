# Урок 3. Задание № 3
# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.
# -------------------------------------------------------------
# Задание выполнил студент GeekBrains  Турчин Богдан.
# -------------------------------------------------------------
import random

SIZE = 10           # Размер массива
MIN_ITEM = 0        # Минимальное  значение массива
MAX_ITEM = 100      # Максимальное значение массива
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]   # Создаю массив

print(array)
min = 0
max = 0

for i in range(1, SIZE):
    if array[i] < array[min]:
        min = i
    elif array[i] > array[max]:
        max = i

print('Мин = ', min, '\nМакс =', max)

array[min], array[max] = array[max], array[min]

print('Новый массив: \n', array)

# --- Пробная версия с рекурсией -------
print('\nС помощью рекурсии!')

def my_max (arr):
    if not arr:
        return None
    else:
        max_n = my_max(arr[1:9])
        if max_n > arr[0]:
            return max_n
        else:
            return arr[0]

# print(array[1:8:2])

print(my_max(array))

