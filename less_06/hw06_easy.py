# ------------------------------
# Lessons 06
# __autor__ - Турчин Богдан П.
# -------------------------------
import math

print("*-------------------------------*")
print("*    Шестое домашнее задание    *")
print("*        hw06_easy.py           *")
print("*           Задача 1            *")
print("*-------------------------------*")

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

#Определяю класс для фигуры треугольника
class Triangle:
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy
        # Вычисление сторон
        self.AB = round(math.sqrt(int(math.fabs(((By - Ay) ** 2) + ((Bx - Ax) ** 2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((Cy - By) ** 2) + ((Cx - Bx) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((Ay - Cy) ** 2) + ((Ax - Cx) ** 2)))), 2)

    def perimetr(self): # Периметр
        self.perimetr = (self.AB + self.BC + self.CA)
        return (self.perimetr)

    def area(self):     # Площадь
        self.perimetr /= 2
        self.area = round(math.sqrt(
        self.perimetr * (self.perimetr - self.AB) * (self.perimetr - self.BC) * (self.perimetr - self.CA)), 2)
        return self.area

    def heigtt(self):   # Высота
        self.area *= 2
        self.heigtt =round((self.area / self.CA), 2)
        return self.heigtt

my_tri = Triangle(3,2,5,6,9,2)

print('Длинны строн АВ = {}, ВС = {}, СА = {}'.format(my_tri.AB, my_tri.BC, my_tri.CA))
print(f'В треугольнике со сторонами ABC: \nПериметр: {my_tri.perimetr()} см \nПлощадь: {my_tri.area()} кв. см')
print(f'Высота: {my_tri.heigtt()} см')

print('-' * 43)

my_tri = Triangle(12,8,18,11,16,5)

print('Длинны строн АВ = {}, ВС = {}, СА = {}'.format(my_tri.AB, my_tri.BC, my_tri.CA))
print(f'В треугольнике со сторонами ABC: \nПериметр: {my_tri.perimetr()} см \nПлощадь: {my_tri.area()} кв. см')
print(f'Высота: {my_tri.heigtt()} см')

print()

print("*-------------------------------*")
print("*    Шестое домашнее задание    *")
print("*        hw06_easy.py           *")
print("*           Задача 2            *")
print("*-------------------------------*")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy
        self.Dx = Dx
        self.Dy = Dy
        self.AB = round(math.sqrt(int(math.fabs(((Bx - Ax) ** 2) + ((By - Ay) ** 2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((Cy - By) ** 2) + ((Cx - Bx) ** 2)))), 2)
        self.CD = round(math.sqrt(int(math.fabs(((Dy - Cy) ** 2) + ((Dx - Cx) ** 2)))), 2)
        self.DA = round(math.sqrt(int(math.fabs(((Ay - Dy) ** 2) + ((Ax - Dx) ** 2)))), 2)

    def checklanktrap(self):
        if (self.AB == self.CD) or (self.BC == self.DA):
            return 'Трапеция равнобочная'
        else:
            return 'Трапеция не равнобочная'

    def perimetr(self): # Периметр
        self.perimetr = round(self.AB + self.BC + self.CD + self.DA, 2)
        return (self.perimetr)

    def heigt(self):   # Высота
        self.heigt =round(math.sqrt(self.AB ** 2 - (((self.DA - self.BC) ** 2 + self.AB ** 2 - self.CD ** 2) / (2 * (self.DA - self.BC))) ** 2), 3)
        return self.heigt

    def area(self):     # Площадь
        #self.perimetr /= 2
        self.area = round((self.AB + self.BC) / 2 * self.heigt, 2)
        return self.area

my_trap = Trapeze(4,2,6,6,11,6,13,2)
print('-' * 55)
print('Длинны строн АВ = {}, ВС = {}, СD = {}, DА = {}'.format(my_trap.AB, my_trap.BC, my_trap.CD, my_trap.DA))
print(my_trap.checklanktrap())
print(f'Высота: {my_trap.heigt()} см')
print(f'В трапеции со сторонами ABCD: \nПериметр: {my_trap.perimetr()} см \nПлощадь:  {my_trap.area()} кв. см')


print()
print('Вторая трапеция!')
print('-' * 55)
my_trap = Trapeze(4,2,8,10,16,10,20,2)
print('Длинны строн АВ = {}, ВС = {}, СD = {}, DА = {}'.format(my_trap.AB, my_trap.BC, my_trap.CD, my_trap.DA))
print(my_trap.checklanktrap())
print(f'Высота: {my_trap.heigt()} см')
print(f'В трапеции со сторонами ABCD: \nПериметр: {my_trap.perimetr()} см \nПлощадь:  {my_trap.area()} кв. см')
