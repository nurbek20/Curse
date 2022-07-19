# #     """Class"""

# class Dough:
#     muka=400
#     salt=15
#     eggs=2
#     butter=50
#     raz=15
#     milk=200
#     sugar=150
#     lemon=2
    
    
#     def mix(self):
#         print("We must to mix all recepts") 
#     def add_muka(self):
#         self.muka=self.muka+50
#         print("В конце получилось", self.muka, "гр") 
#     def add_eggs(self,count):
#         self.eggs=self.eggs+count
#         print("Кол-во яиц", self.eggs)       
# pie=Dough()                                              # создали обьект класа Dough
# print("количество сахар ",pie.sugar,"гр")
# print("количество мука ",pie.muka,"гр")
# print("количество туз ",pie.salt,"гр")
# print("количество яйцо",pie.eggs,"шт")
# print("количество масло ",pie.butter,"гр")
# print("количество разнехнител ",pie.raz,"гр")
# print("количество молоко ",pie.milk,"гр")
# print("количество лимон ",pie.lemon,"шт")
# pie.mix()
# pie.add_muka()
# pie.add_muka()
# pie.add_eggs(1)


# class Notebook:
#     cpu=5
#     ram=12
#     graphics_card=10_3897
#     cdd=223
#     matherboard=True
#     screen_size=1920,1080

#     def my_book(self):
#         print("процессор: " ,hp.cpu)
#         print("оперативный память: " ,hp.ram ,"гб")
#         print("видое карта: " ,hp.graphics_card)
#         print("жесткий диск: " ,hp.cdd,"гб")
#         print("материнская плата: " ,hp.matherboard)
#         print("размер экрана: " ,hp.screen_size)

# hp=Notebook()
# hp.my_book()


# class Human:
#     name1=None
#     age1=None
#     def __init__(self,name,age):     #конструктор класса Human
#         self.name1=name
#         self.age1=age
#     def description(self):
#         print("Имя человека: ",self.name1)
#         print("Возраст человека: ",self.age1)
# human=Human("Асан",25)
# human.description()

# human2=Human("Аиша",20)
# human2.description()

class Cat:
    name2=None
    color2=None
    def __init__(self, name,color):
        self.name2=name
        self.color2=color
    def description(self):
        print("имя: ",self.name2)
        print("color:",self.color2)
name=Cat("Матроскин", "black")
name.description()

# Создайте класс Laptop, у которого есть:
# конструктор init, принимающий 3 аргумента: бренд, модель и цену ноутбука.
# На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price.
class Laptop:
    brand1=None
    model1=None
    price1=None
    def __init__(self,brand,model,price):
        self.brand1=brand
        self.model1=model
        self.price1=price
    def description(self):
        print('бренд: ',self.brand1)
        print('модел: ',self.model1)    
        print('цена ноутбука: ',self.price1)  
name=Laptop('HP','Pavilion 14 с Intel Core i7-1065G7 ','45 тысяч')  
name.description()

# Создайте класс SoccerPlayer, у которого есть:
# конструктор init, принимающий 2 аргумента: name, surname. Также во время 
# инициализации необходимо создать 2 атрибута экземпляра: goals и assists -
# общее количество голов и передач игрока, изначально оба значения должны быть 0
# class SoccerPlayer:
# Создайте класс Lion. В нем должен быть метод roar,
# который печатает на экран "Rrrrrrr!!!"
class Lion:            
    name="Rrrrr!"
    def my_lion(self):
        print("лев:",self.name)
Matroskin = Lion()
Matroskin.my_lion()