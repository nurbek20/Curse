# # """ООП - Обьектно-ориентированное програмирования"""
# # """Класс, обьекты"""
# # """ В ООП есть 4 основных концепций """
# # Наследования
# # Абстраксия, Композиция
# # Полиформизм
# # Инкапсуляция

# class Animal:
#     feet = 4         #атрибуты класса
#     tail = 1
#     head = 1
#     ears = 2
#     eyes = 2
#     arn = 2
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def run(self):
#         self.feet = 2         #метод классa Animal
#         print(f"He run very fast, it has {self.feet} feet")
# cat=Animal("Мурка","Черный")
# print(cat.tail)
# print(cat.feet)
# print(cat.name)
# print(cat.color)
# cat.run()


# class Dough:             # родительский класс
#     muka = 600
#     salt = 2
#     butter = 200
#     water = 300

#     def mix(self):
#         print("Mix all recepts")

# class Samsy(Dough):    # дочерный класс 
#     eggs = 2


# samsy= Samsy()
# samsy.mix()
# print(samsy.muka)

# class Pie(Dough):
#     sugar = 250
#     milk = 200
#     vanillin = 5
#     bakingPowder= 5
#     # baking_powder= 5
# pie = Pie()
# pie.mix()
# print(pie.muka)
# print(Pie)
# class Vanhicle:
#     pass

# class Car(Vanhicle):
#     pass

# class Plane(Vanhicle):
#     pass

# class Boat(Vanhicle):
#     pass

# class RaceCar(Vanhicle):
    # pass

# class Person:
#     name="Айбек"
#     age="25"
#     def __str__(self):
#         return self.name
# aibek=Person()
# print(aibek.name)    
# print(aibek)
# class Person:
#     def __init__(self,name,surname,gender='male'):
#         self.name=name
#         self.surname=surname
#         # self.gender=gender
#     # def __str__(self):
#         if gender =="male" or gender == "famele":
#             self.gender=gender
#         else:
#             print("Не знаю, что вы имели виду")
#             self.gender="male"
#     def __str__(self):
#         if self.gender=="male":
#             return f"Гражданин {self.surname} {self.name}"
#         elif self.gender == "famele":
#             return f"Гражданка {self.surname} {self.name}"        
# per=Person("Aida","Aibek","male")
# # print(per.name)
# # print(per.surname)
# print(per.gender)
# print(per)

# class Publication:
#     def __init__(self,name,date,pegas,library,type):
#         self.name=name
#         self.date=date
#         self.pegas=pegas
#         self.library=library
#         self.type=type
# # print(type(Publication))
# class Book(Publication):
#     def __init__(self,type='book'):
#         self.type=type
# class Magazine(Publication):
#     def __init__(self,type='magazine'):
#         self.type=type
# class Newspaper(Publication):
#     def __init__(self,type="newspaper"):
#         self.type=type 
# n=Publication()
# print(n)        
# vowel=["a","e","i","o","u","y"]
# class Letter :
#     def __init__(self,letter):
#         self.letter=letter
#         if isinstance(letter,str):
#             if letter.isalpha():
#                 if letter in vowel:
#                     print("Это буква гласная")
#                 else:
#                     print("Это буква согласная")
#         else:
#             print("Вветите буква еще раз")            
# n=Letter(4)

# class Student:
#     def __init__(self,age,grade,scoolname):
#     self.age=age
#     grade=0
#     scoolname=""

# Anna= Student 
# Anna.age=18
# Anna.grade=2
# Anna.scoolname="MGU"   
# print(Anna.age,Anna.grade,Anna.scoolname)


# class Band:
#     def __init__(self):

