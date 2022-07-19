# class Counter:
#     def start_from(self,count=0):
#         self.count = count
#     def increment(self):
#         self.count=self.count + 1  
#     def display(self):
#         print(f"Текущее значения счетчика = {self.count}")
#     def reset(self):
#         self.count = 0

# count=Counter() 
# count.start_from(5)
# count.display()
# count.increment()
# count.display()
# count.reset()
# count.display()

#   """Принципы ООП - инкапсуляция  """
#Инкапсуляция - это упаковка даннык и функций , работающих с этим данными, 
#в один компонент и ограничения доступа к некоторым компонентам объекта.
#Инкасуляция - Скрытые информации
#Ест 3 уровня доступа к данным
#публичный {public, нет особо синтаксиса, publikDate}:
#защищеный (protected, одно нижнее подчеркивание в начале, _protectedData)
#приватный (private, два нижних подчеркивания в начале названия __protectedData)
# class Bankomat:
#     def __init__(self,name,_id,__password):
#         self.name=name
#         self._id=_id
#         self.__password=__password

#     def pulic_method(self):
#         print(f"Ползователь: {self.name}")   
#     def _protectedMethod(self):
#         print(f"Ползователь: {self.name}, \nid: {self._id}")   
#     def __privateMethod(self):
#         print(f"Ползователь: {self.name}, \nid: {self._id}, \nпароль: {self.__password} ")
# bank=Bankomat("Alex","452301257","qwertyi4521")
# bank.pulic_method()
# bank._protectedMethod()
# # bank.__privateMethod()
# bank._Bankomat__privateMethod()

# """Геттер и Сеттеры"""
# get - получить
# set - назначать, принимать, передать

# class Number:
#     def set(self,number):
#         self.number = number
#     def get(self):
#         return self.number

# num=Number()
# num.set(5)
# print(num.get())  

# class Salary:
#     def set(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def get(self):
#         return f"имя: {self.name} зарабатывает в месяц {self.salary}"
#     def countofYear(self):
#         return f"Имя: {self.name} зарабатывает в год {self.salary*12}"
# name2=input("Input name: ")
# salary2= int(input("Input salary: "))            
# name= Salary()
# name.set(name2, salary2)
# print(name.get())
# print(name.countofYear())

# Создайте класс UserMail, у которого есть:
# Конструктор __init__, принимающий 2 аргумента: логин и почтовой адрес. 
# Их необходима сохранить в экземпляр как атрибуты login и __email (обратите 
# внимание, приватный атрибут) 
# метод геттер get_email, которое возвращает приватный атрибут __email; 
# метод сеттер set_email, которое принимает в виде строки новую почту.
# Метод должен проверят, что в новой почте есть только один символ @ и после 
# нее есть точка, то это должен возвращать ошибку. Если данные  условия выполняются, 
# новоя почта сохраняется в атрибут __email, в противном случае 
# выведите сообщение "Ошибочная почта"; 
# 
                  
# class UserMail:
#     def __init__(self,login,__email):
#         self.login = login
#         self.__email = __email
#     def get_email(self):
#         return self.__email
#     def set_email(self):
#         self.__email = ""
#         i = self.__email.find("@")
#         n = self.__email[0:i]
#         if len(n) < 1:
#             self.__email = self.__email
#         else:
#             print("Ошибочная почта")
# mail = UserMail("qwerty123","@gmail.com")
# print(mail.set_email())