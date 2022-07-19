# """*args-Позиционные элементы, **kvargs - Имменованние элементы"""
# lst=[45,85,62,17]
# print(*lst)
# print(*lst, sep=',')
# print(lst)
# def my_func(a, lst):
#     sum1=a
#     for i in lst:
#         sum1 = sum1 + i
#     print(sum1)

# my_func(5, [1,2,3,4])
# def my_func(a, lst):
#     sum1=1
#     for i in lst:
#         sum1 = sum1 * i
#     print(sum1 * a)
# my_func(5, [1,2,3,4])    
# def name():
#     n=input(': ')
#     return n
# print(name())
# def my_func2(a,*lst):
#     sum1=a
#     for i in lst:
#         sum1 += i
#     print(sum1)    
# my_func2(5,1,2,3,4,8,7)  

#  """**kwargs"""

# dct={"name": "Anna","age":15}
# print(dct)
# # print(**dct)
# def my_func3(*args,**kwargs):
#     print(*args)
#     for i in kwargs.values():
#         print(i)
# my_func3(4,5,6,7,name="Anna",age=15)        
 
# def my_func3(*args,**kwargs):
#     print(*args)
#     for i in kwargs:
#         print(kwargs[i])
# my_func3(4,5,6,7,name="Anna",age=15)

# def num2(a,*args):
#     summ=0
#     for i in args:
#         if i % 2==0:
#             summ += i
#     print(summ-a)
# num2(3,8,9,4,6)        
# def my_func4(**kwargs):
#     for i in kwargs:
#         print(i,"-",kwargs[i])
# my_func4(name="Jon",surname="Vud", age="22",phone="1234567890")
# def my_func5(*args):
#     summ=0
#     for i in args:
#         summ += i
#     print(summ)
# my_func5(3,2)        
# my_func5(4,5,6,7)        
# my_func5(1,2,3,5,6)

     # """Traceback"""
# from Month1.hw15 import is_prime


# a=5
# b=0
# if b == 0:
#     print("нельзя")
# else:
#     print(b/a)    
# print(a+b)
# print(a*b)
# print(b/a)

# if b == 0:
#     raise ZeroDivisionError("На ноль делить нельзя")
# else:
#     print(b/a) 

# if isinstance(b,str):
#     raise TypeError("Тип данных должен быть 'int'")
# else:
#     print(a/b) 

# def summ(a,b):
#     if isinstance (a, str):
#         raise TypeError ("Тип данных должен быть 'int'")
#     if isinstance (a, bool):
#         raise TypeError ("Тип данных должен быть 'int'")
#     if isinstance (b, bool):
#         raise TypeError ("Тип данных должен быть 'int'")
#     if isinstance (b, str):
#         raise TypeError ("Тип данных должен быть 'int'")
#     print(a+b)
# summ("5",5)


# Напишите функцию, которая принимает параметр n и выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
#  (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное
#  целое число n — столько элементов последовательности должна отобразить программа. 
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.

# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

# a=int(input("Введите число: "))
# b=''
# for i in range(a+1):
#     b = b + (str(i) + ' ') * i
# print(b[0:a*2])
# print(b)
# print(len(b))
# a=5
# lst=[]
# for i in range(a):            # 0 ,1 ,2 ,3, 4
#     for y in range(i):        # for y in range (2):   
#         lst.append(i)
# print(*lst[0:a], sep=",")  