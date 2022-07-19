# Задание 5
# Напишите программу с классом Car. Создайте конструктор класса Car. 
# Создайте атрибуты класса Car — color (цвет), type (тип), year (год). 
# Напишите пять методов. Первый — запуск автомобиля, при его вызове
#  выводится сообщение «Автомобиль заведен». 
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». 
# Третий — присвоение автомобилю года выпуска. 
# Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.:
class Car:
    # y=None
    # t=None
    # c=None
    def __init__(self,year,typee,color):
        self.y=year
        self.t=typee
        self.c=color
    def first_z(self):
        print('автомабиль заведон')
    def second_z(self):
        print("автомабиль заглужен")
    def description(self):
        print('год',self.y)
        print('тип',self.t)
        print('цвет',self.c)
car=Car(2017,'Featon','black')
car.first_z()
car.second_z()
car.description()
# 1
# Найти площадь треугольника
# import math 
from math import sqrt
print("Длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print("Площадь: %.2f" % s)

# Задание 2:

# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод init(), внутри которого будут определены два 
# динамических свойства:
#  1) lang - язык и 2) letters - список букв. Начальные значения 
# свойств берутся из входных
#  параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
class Alphabet:
    def __init__(self ,lang,letters):
        self.lan=lang
        self.let=letters
    def print(self):
        print('алфавит',self.let)  
    def letters_num(self):
        print('количество',len(self.let))
al=Alphabet("english",["a","b","c"])
al.print()
al.letters_num()

# 3
# Создайте класс Factory и внутри создайте 2 метода:
# a.Метод engine который возвращает строку "Двигатель создан"
# b.Метод bridge который возвращает строку "Ходовая часть создана"
class Factory:
    eng=None
    brid=None
    def __init__(self,engine,bridge):
        self.eng=engine
        self.brid=bridge
    def num2(self):
        print("engine: ",self.eng)    
        print("bridge: ",self.brid) 
n=Factory("Двигател создан","ходовая часть создана")           
n.num2()

# Задание 4:
    # Напишите программу, которая циклично запрашивает у пользователя любой символ
    # и выводит этот символ.
    # Завершает работу при вводе нуля.
while True:
    a=int(input("Введите число: "))
    if a > 0:
        print(a)        
    else:
        quit()