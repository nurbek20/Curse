#  Тернарный оператор , List comprehension
# lst=[5,8,7,12,56,87,55,10,4,3]
# lst2=[item for item in lst]
# lst3=[item for item in lst if item > 5]
# q=5
# print(isinstance(q,int))
# print(lst2)
# print(lst3)

# for i in lst:                # Цикл по элементу
#     if i > 5:
#         lst2.append(i)
# print(lst2)

# for i in range(len(lst)):     # Цикл по индексу
#     if lst[i] > 5:
#         lst2.append(lst[i])
# print(lst2)  

# []- list
# {k:v} - dict
# {}- tuple
# {1,5,8,5,True}-set
# ls=[[45,58],[4,87],[1,2]]
# ls2=[y for i in ls for y in i]
# ls3=[]
# for i in ls:
#     for y in i:
#       ls3.append(y)
# # print(ls3)
# even_ls=[]        
# for i in ls:
#     for y in i:
#         if y % 2 ==0:
#             even_ls.append[y]
# print(even_ls) 

# even_ls=[y for i in ls for y in i  if  y % 2 == 0 and y > 3]
# print(even_ls)
# t=["kg","ru","en","kz"]
# t2=[i.upper() for i in t]
# print(t2)

   #Тернарные условия
# num=5
# if num>3:
#     print("It's good")
# else:
#     print("So good") 

# n=5
# print("Yes" if n > 6 else n)  
# print("It's good" if num >3 else "So good")
# b=5 
# print(b if b==5 else "FizzBuzz")

# """break, continue"""
# s="Python"
# n=input("напишите язык програминования: ")
# while True:
#     if n=="python".upper():
#         print("Да верно")
#         break
#     else:    
#         n=input("напишите язык програминования: ")

# message = "h"
# print(message+"x"+message*2)
# print("ox"+message*2)                
# p="python"
# for i in p:
#     if i == message:
#         break
#     else:
#         print(i)
# for i in p:
#     if i == message:
#         continue
#     else:
#         print(i)

# def func1(res):
#     if res == 1:
#         return 1
#     else: 
#         return res*func1(res*1)
# print(func1(4)) # рекурсия это само себя умножает либо вычесляет до заданого число

# s="Python"
# n=input("напишите язык програминования: ")
# while True:
#     if n=="python".upper()  and n=="python".title() and n=="python".lower():
#         print("Да верно")
#         break
#     else:    
#         n=input("напишите язык програминования: ")
# s="Python"
# n=input("напишите язык програминования: ").lower()
# while True:
#     if n.title()==s:
#         print("Да верно")
#         break 
#     else:    
#         n=input("напишите язык програминования: ").lower()