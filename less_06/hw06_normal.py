# ------------------------------
# Lessons 06
# __autor__ - Турчин Богдан П.
# -------------------------------
import math

print("*-------------------------------*")
print("*    Шестое домашнее задание    *")
print("*       hw06_normal.py          *")
print("*           Задача 1            *")
print("*-------------------------------*")

# Задание-1:
# Реализуйте описанную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class People:    # Человек
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronyumic = patronymic
        #print("Класс People создан")

    def get_full_name(self):    # Полное имя
        return self.surname + ' ' + self.name + ' ' + self.patronyumic

    def get_short_name(self):   # Краткое имя
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronyumic[0].upper())

class Pupil(People):    # Учениек
    def __init__(self, surname, name, patronymic, mom, dad, school_class):
        People.__init__(self, surname, name, patronymic)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class


class Teacher(People):
    def __init__(self, surname, name, patronymic, subject):
        People.__init__(self, surname, name, patronymic)
        self.subject = subject

class School:         # Класс    ученик  учитель
    def __init__(self, classroom, pupil, teacher):
        self.classroom = classroom
        self.pupil = pupil
        self.teacher = teacher

class Class_rooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}


people_one = People('Сергей', 'Иванов', 'Александрович')
people_two = People('Владимир', 'Петров', 'Анатольевич')

print('Первый способ вывода Ф.И.О.')
print(people_one.surname, people_one.name, people_one.patronyumic)
print(people_two.surname, people_two.name, people_two.patronyumic)
print('-' * 40)
print('Второй способ вывода Ф.И.О.')
print(people_one.get_full_name())
print(people_two.get_full_name())
print('-' * 40)
print('Краткая форма вывода Ф.И.О.')
print(people_two.get_short_name())
print(people_one.get_short_name())

print('-' * 40)
if __name__ == '__main__':  # Тестирование.
    teachers = [Teacher('Тихомиров', 'Александр', 'Иванович', 'Математика'),
                Teacher('Гузик', 'Петр', 'Николаевич', 'Литература'),
                Teacher('Колпачев', 'Евгений', 'Александрович', 'Физика'),
                Teacher('Данилюк', 'Дмитрий', 'Борисович', 'История'),
                Teacher('Николаев', 'Михаил', 'Юрьевич', 'Биология')]

    classes = [Class_rooms('4 А', [teachers[0], teachers[1], teachers[2]]),
               Class_rooms('4 Б', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('5 А', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('5 Б', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('6 А', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('6 Б', [teachers[3], teachers[1], teachers[0]]),
               Class_rooms('7 А', [teachers[3], teachers[1], teachers[0]]),
               Class_rooms('7 Б', [teachers[1], teachers[3], teachers[4]])]

    parents = [People('Савельева', 'Светлана', 'Игоревна'),
               People('Савельев','Артур','Владимирович'),
               People('Петрова','Анастасия','Анатольевна'),
               People('Петров', 'Игорь', 'Семенович',)]

    pupils = [Pupil('Сидоров', 'Алексей', 'Николаевич', parents[0], parents[0], '4 Б'),
              Pupil('Булычев', 'Кирилл', 'Анатольевич', parents[1], parents[1], '5 А')]

print('Список классов в школе:')
for k in classes:
    print(k.class_room)

print()

for f in classes:
    print('Учителя, преподающие в {} классе:'.format(f.class_room))
    for teacher in classes[0].teachersdict.values():
        print(teacher.get_full_name())

print()

for f in classes:
    print("Ученики в классе {}:".format(f.class_room))
    for st in pupils:
        print(st.get_short_name())


