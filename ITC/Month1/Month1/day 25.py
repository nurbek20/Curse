# i=0
# countries=["Бразилия","Суринам","Уругвай","Эквадор","Суринам","Чили"]
# # for i in range(len(countries)):
# #     print(countries[i])

# for i in range(1,len(countries)):
#     if i % 2 ==0:
#         print(countries[i])    
# Зная массив nums, для каждого nums [i] узнайте, сколько чисел в массиве меньше его. 
# То есть для каждого числа [i] необходимо подсчитать количество действительных j 
# таких, что j! = I и nums [j] <nums [i].
# Вернуть ответ в виде массива.
# Пример 1:
# Ввод: nums = [8,1,2,2,3]
# Выход: [4,0,1,1,3]
# Объяснение:
# Для nums [0] = 8 существует четыре числа меньших, чем это (1, 2, 2 и 3).
# Для nums [1] = 1 не существует меньшего числа, чем это.
# Для nums [2] = 2 существует одно меньшее число, чем оно (1).
# Для nums [3] = 2 существует одно меньшее число, чем оно (1).
# Для nums [4] = 3 существует три меньших числа, чем это (1, 2 и 2).
# class Solution(object):
#     def smallerNumbersThanCurrent(self, nums):
#         res=[]
#         for i in range(len(nums)):
#             count = []
#             for j in range(len(nums)):
#                 if nums[i] > nums[j]:
#                     count.append(nums[j])
#             res.append(len(count))
#         print(res)
# n=Solution()
# n.smallerNumbersThanCurrent([8,1,2,2,3])   
# lst=[[1,2,3],[3,2,1]]             
# for i in lst:
#     summ=0
#     for y in i:
#         summ = summ + y
#     print(summ)
# c=0
# while True:
#     if c == 25:
#         break
#     print(c)
#     c = c + 1
# while True:
#     f="Kirilovskaya"
#     n= "Anna"
#     a=input("Введите имя:  ")
#     b=input("Ведите фамилия:  ")
#     if a == n or b == f:
#         print(f"Имя {a} \nФамилия {b}")    
#         break   
#     else:
#         print("Не правилное имя введите заново")        
# a = [ 2,4,5,-45,-67,-4, -8, 67, 4, 45] 
# positive_number=[]
# negative_number=[]
# for i in a:
#     if i >0:
#         positive_number.append(i)
#     if i<0:
#         negative_number.append(i)    
# print(positive_number)
# print(negative_number)
# while True:
#     for i in a:
#         if i >0:
#             positive_number.append(i)
#         if i<0:
#             negative_number.append(i)   
#     print(positive_number)
#     print(negative_number)
# #     break
# while True:
#     count=0
#     for i in range(1,100):
#         count += i
#         print(count)
#     break

# numbers=[67,99,56,43,66,12]
# summ=0
# for i in numbers:
#     summ += i
# print(summ)
# while True:
#     for i in numbers:
#         summ += i
#     print(summ)    
#     break
# a = int(input("Введите число: "))
# for i in range(1,10):
#     print(f'{i} * {a} = {i*a}')

# number=int(input("Введите число: "))
# i = 1
# while i < 10:
#     print(f'{i} * {number} = {i*number}')
#     i = i + 1 
# def my_func():
#     print("Мой первый функция!!")
# my_func()    
# my_func()    
# def my_sum():
#     a = 5
#     b = 8
#     print(a+b)
# def my_div():
#     a = 5
#     b = 8
#     print(a/b)
# def my_mult():
#     a = 5
#     b = 8
#     print(a*b)        
# my_sum()    
# my_div()    
# my_mult()    
# def my_sum2():
#     a = 5
#     b = 8
#     return a + b
# print(my_sum2()) 
# def my_sum3(a,b):
#     print(f"Сумма двух чисел {a} и {b}:", a + b)
#     print(f"Деления двух чисел {a} и {b}: ", a / b)
#     print(f"Производения двух чисел {a} и {b}: ",a * b)
#     print(f"Вычитания двух чисел {a} и {b}: ",a - b)
# num1=int(input("Введите число: "))    
# num2=int(input("Введите второе число: "))    
# my_sum3(num1,num2) 

# def text(txt):
#     print("Вы написали: ",txt)
# # text("Hello world") 
# t=input("Напишите Называние города: ").title()
# text(t)

# def reverse_text(txt):
#     print(txt[::-1])
# reverse_text("123qwerty")    
# def my_length(lst):
#     print(len(lst))
# my_length([45,48,"Tina",False])
# def my_length1(lst):
#     isinstance (lst, str)
#         # raise TypeError ("Тип данных должен быть 'int'")
#     isinstance (lst, bool)
#         # raise TypeError ("Тип данных должен быть 'int'")
#     print(isinstance(lst))
# my_length1([45,48,"Tina",False])
# """isinstance""))
# print(isinstance("False",str))"
# print(isinstance(545,int))

