# """ООП - Полиформизм"""
# # Наследования
# # Инскапсуляция 
# # Композиция 
# # Полиформизм
# """
# Полиформизм ознлочает, что одно и то же имя функция (но разные сигнатуры )
# изпользуется для разных типов.
# """
# def concat(a,b):
#     print(a+b)

# concat(5,8)                     # арифметическая операция
# concat("web","developer")       # конкатенация
# # len
# # Встроенное полиморфные функции
# ls = [45, 8545, 852]    # 3
# str1 = "my book"        # 7
# str2 = "45 8545 852"    # 11
# # count
# ls2 = [45, 8, 8, 45, 77, "python", "python", True]
# str3 = "Hello world"
# print(ls2.count(45))
# print(str3.count('l'))
# # pop
# ls4 = [54, 8, 5212, 85]
# ls4.pop()
# print(ls4)
# ls4.pop(0)  # список
# print(ls4)

# set2={54, 5452 , True, "good"}
# set2.pop()    # set
# print(set2)
# Встоенный модуль math
# import day26
# from day26 import Zoo
# from day26 import my_variable
# zoo2 = Zoo('Тигр','','')
# print(zoo2.animal_1)
# print(my_variable)
# import math
# # print(math.pow(5, 3))        # 5 * 5 * 5 = 125
# # print(5 ** 3 )               # 5 * 5 * 5 = 125
# # print(5 * 5 * 5)             # 5 * 5 * 5 = 125
# # print(math.factorial(5))
# # # 5! = 1 * 2 * 3 * 4 * 5 = 120
# # 3! = 1 * 2 * 3 = 6
# # print(math.pi)    # 3. 141592653589793
# # # C = 2 * pi * r
# # # S = pi * r ** 2    1) r ** 2 = x   2) pi * x
# # # S = pi * r * r
# # # S = pi * math.pow(r, 2)
# # radius = float(input("Введите радиус круга: "))
# # P = float(input("Введите радиус круга: "))
# # C = 2 * math.pi * radius
# # S = math.pi * math.pow(radius, 2)
# # radius = P /( 2 * math.pi)
# # print("Длина окружночсти равна : "+str(C))
# # print("Длина окружночсти равна : " , C)
# # print("Плошат круга",S)
# # print("Радиус окружности равен: ",radius)
# print(math.sqrt(64))      # 8
# print(math.sqrt(100))     # 10
# print(math.sqrt(49))      # 7
# print(math.sqrt(0))       # 0
# print(math.sqrt(1))       # 1
# print(math.sqrt(4))       # 2
# p = math.pi
# print(p)                         # 3.141592653589793
# print(math.ceil(p))              # округления в большую сторону
# print(math.floor(p))             # округления в меньшую сторону
# print(math.ceil(5.6))            # 6
# print(math.floor(5.6))           # 5
# # """split(), join() - метод"""
# txt="python developer"
# # print(txt.split())
# print(len(txt))     # 16
# splitted = txt.split()
# print(len(splitted))

# print(splitted)
# txt2 = "python-developer"
# print(len(txt2.split()))
# print(len(txt2.split("-")))
# print(txt2.split("o"))
# ss = txt2.split("-")       # str -> list
# print(",".join(ss))        # list -> str

# """function open() """
# open(file_name, mode)
# mode - вид, режим
# mode - режим 

# my_file = open("file.txt", "r")
# print(my_file)
# print(my_file.read())
# my_file.close()
# # my_file.read()
# # my_file.close()

# my_file2 = open("file.txt", "a")
# my_file2.write("I am Nurbek")
# my_file2.write("\nWe are students")
# # print(my_file2.read())
# my_file2.close()

# my_file3 = open("file.txt","r")
# # print(my_file3.read())
# for i in my_file3:
#     print(i," of ITCBootcamp")

# my_file4 = open("file.txt","a")
# my_file4.writelines("of ITCBootcamp")
# my_file4.close()
# my_file5 = open("new_file.txt","x")


lang_list = ["python","java","c#","javascript","swift","c++"]