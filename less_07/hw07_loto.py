# ------------------------------
# Lessons 07
# __autor__ - Турчин Богдан П.
# -------------------------------
import math

print("*-------------------------------*")
print("*   Седьмое домашнее задание    *")
print("*        hw07_loto.py           *")
print("*           Задача 1            *")
print("*-------------------------------*")
"""
== Игра лото ==
Правила игры.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

-------------------------
   9 43 62         74 90
2    27    75 78   82
  41 56 63    76      86 
-------------------------
"""
import random
import sys

barrels = 90    # todo Количество боченочков
p1 = 15         # todo Количество моих ходов
p2 = 15         # todo Количество ходов компьютера

# todo создаю список длиной k(90) из последовательности (90)
barrs = random.sample(range(barrels), barrels)  # todo список последовательности номеро вытаскиваемых боченочков

game_set = random.sample(range(barrels), 30)# todo формирую список номеров двух карточек
# todo Разделяю цифры по двум карточкам
card1 = random.sample([i for i in game_set], 15)  # todo формирую цифры  в первой карточке
card2 = [i for i in game_set if not i in card1]   # todo формирую цифры во второй карточке

#  Формирую карточки по 5 цифр
card1_f = [card1[:5], card1[5:10], card1[10:]]  # todo Карточка игрока
card2_f = [card2[:5], card2[5:10], card2[10:]]  # todo Карточка ПК

#  Формирую распределение 5 номеров в карточке в строке из 9и клетках случайным образом
for card1_line in card1_f:
    card1_line.sort()
    card1_line.insert(random.randint(0, 4), ' ')
    card1_line.insert(random.randint(0, 5), ' ')
    card1_line.insert(random.randint(0, 6), ' ')
    card1_line.insert(random.randint(0, 7), ' ')

#  Карточка компьютера
for card2_line in card2_f:
    card2_line.sort()
    card2_line.insert(random.randint(0, 4), ' ')
    card2_line.insert(random.randint(0, 5), ' ')
    card2_line.insert(random.randint(0, 6), ' ')
    card2_line.insert(random.randint(0, 7), ' ')

# todo Команды для тестирования
#print(barrs)
#print(game_set)
#print(card1)
#print(card2)
#print('Первая карточка \n', card1_f)
#print('Вторая карточка \n', card2_f)
#print(card1_line, '- Первая карточка')
#print(card2_line, '- Вторая карточка')

# todo Функции
def card(p):    # todo Прорисовка карточек
    if p == 0:
        print('{:-^26}'.format(' Ваша карточка '))
        for l1 in card1_f:
            for n1 in l1:
                print('{0:>2}'.format(n1), end=' ')
            print()
        print('-' * 26)
    if p == 1:
        print('{:-^26}'.format(' Карточка компьютера '))
        for l2 in card2_f:
            for n2 in l2:
                print('{0:>2}'.format(n2), end=' ')
            print()
        print('-' * 26)


def you_go(): # todo Ваш ход
    a = input('Зачеркнуть цифру? (y/n): ')
    if a == 'y' or a == 'Y':
        if barr in card1:
            for l in card1_f:
                try:
                    l.insert(l.index(barr), '><')
                    l.pop(l.index(barr))
                except ValueError:
                    continue
            print('\nOk')
            return 1
        else:
            print('\nИгра закончена')
            sys.exit()
    if a == 'n' or a == 'N':
        if barr in card1:
            print('У Вас в карточке имеется №', barr)
            b = input('Хотите продолжить игру? (y/n): ')
            if b == 'y' or b == 'Y':
                print()
                you_go()
            else:
                print('\nИгра закончена')
                sys.exit()
        else:
            print('\nOk')


def comp_go(): # todo Ход компьютера
    if barr in card2:
        for i in card2_f:
            try:
                i.insert(i.index(barr), '><')
                i.pop(i.index(barr))
            except ValueError:
                continue
        return 1


# todo Игра
for barr in barrs:
    barrels -= 1
    print('\nНовый боченок: {} (осталось: {})\n'.format(barr, barrels))
    card(0)
    card(1)
    if you_go() == 1:
        p1 -= 1
    if comp_go() == 1:
        p2 -= 1
    if p1 == 0:
        print('\nВы выиграли! Поздравляю!')
        sys.exit()
    if p2 == 0:
        print('\nВы проиграли! :(')
        sys.exit()
    if barrels == 0:
        print('\nИгра закончена.')
        sys.exit()