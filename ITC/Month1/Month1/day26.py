# 1. Создайте класс Factory и внутри создайте 2 метода:
# a. Метод engine который возвращает строку "Двигатель создан"
# b. Метод bridge который возвращает строку "Ходовая часть создана"
# 2. Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. В классе
# Toyota создайте методы wheels и windows.
# a. Метод wheels возвращает строку "Колёса готовы"
# b. Метод windows возвращает строку "Стёкла готовы"
# Из класса Toyota вызовите все методы, методы вернут вам сроки(объекты)
# Результат каждого метода вставьте в лист
# class Faktory:
#     def engine(self):
#         print("Двигатель создан")
#     def bridge(self):    
#         print("Ходовая часть создан")
# class Tayota(Faktory):
#     def wheels(self):
#         print("Калеса готовы")
#     def windows(self):
#         print("Стекла готовы")    
# n=Tayota()
# n.engine()
# n.bridge()        
# n.wheels()
# n.windows()
# 1. Создайте Класс Zoo.
# 2. Инициализируйте класс в объект.
# 3. К объекту Zoo добавьте атрибут animal_1 и присвойте ему значение "Тигр"
# 4. К объекту Zoo добавьте атрибут animal_2 и присвойте ему значение "Бегемот"
# 5. К объекту Zoo добавьте атрибут animal_3 и присвойте ему значение "Жираф"
# 6. В объекте Zoo измените значение атрибута animal_1 и присвойте ему значение
# "Лев".
# 7. К объекту Zoo добавьте атрибут animal_4 и присвойте ему list состоящий из
# animal_2 и animal_3
# 8. В объекте Zoo измените значение атрибута animal_3 и присвойте ему значение
# "Змея".
class Zoo:
    def __init__(self,animal_1,animal_2,animal_3):
        self.animal_1=animal_1
        self.animal_2=animal_2
        self.animal_3=animal_3
        # return animal_1
# zoo=Zoo("Тигр","Бегамот","Жираф")
# print(zoo.animal_1)        
# print(zoo.animal_2)        
# print(zoo.animal_3)        
# zoo.animal_1="Лев"
# zoo.animal_3="Змея"
# print(zoo.animal_1)
# print(zoo.animal_3)

# """ ООП - композиция """
# """Класс по композиция - это класс у которого атрибут является объектом
# другого класса"""

# class Address:
#     def __init__(self,city,district,street,home_number):
#         self.city=city
#         self.district=district
#         self.street=street
#         self.home_number=home_number
# class Profession:
#     def __init__(self,profession,job_address,salary):
#         self.profession=profession
#         self.job_address=job_address
#         self.salary=salary
# class Worker:
#     def __init__(self,name,city,district,street,home_number,profession,job_address, salary):
#         self.name=name
#         self.address=Address(city=city,district=district,street=street,home_number=home_number)
#         self.profession=Profession(profession=profession,job_address=job_address,salary=salary)

#     def printDate(self):
#         print(f"{self.name} lives in {self.address.city}")
#         print(f"{self.name} lives in the area {self.address.district}")   
#         print(f"{self.name} the street  {self.address.street}")   
#         print(f"{self.name} hom number {self.address.home_number}")   
#         print(f"{self.name} is a {self.profession.profession}")
#         print(f"{self.name} works in the {self.profession.job_address}")
#         print(f"{self.name} get a salary {self.profession.salary}") 
# she= Worker("Anna","Osh","Anar","Salieva", 45 ,"python developer","USA","5000")        
# she.printDate()

# class Human:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def set(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def get(self):
#         print(f"{self.name} is {self.age} years old. He is {self.gender}")  
# he=Human("Alex",20,"male")
# he.get()
# Создать 2 класса Human и Worker. У класса Human, который принимает 
# в конструкторе name, age, gender. И есть методы геттер и сеттер.  
# У метода сеттер есть 3 аргумента: name, age, gender. У метода геттер должен
#  вывести сообщение  "<Name> is <age> years old. He is <gender>"
# У класса Worker есть конструктор который принимает все атрибуты у класса Human.
#  И есть атрибуты profession, about, который является объектом класса Human. 
# И есть метод show_info, он должен возвращать "My name is <name>. I am <age> years old. 
# I am <gender>. I am a <profession>
class Worker:
    def __init__(self,name,age,gender,profession):
        self.name=Human(name=name,age=age,gender=gender)
        self.profession=profession
    def show_info(self):
        print(f"My name is {self.name.name}. I am {self.name.age} yaers old. I am {self.name.gender}. I am a {self.profession} ")
he= Worker("Alex",26,"male","python develooper")
he.show_info()  

my_variable = 'i am a ball'     