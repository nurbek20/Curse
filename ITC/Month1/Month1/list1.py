# def printScores(student, *scores):
#    print(f"Student Name: {student}")
#    for score in scores:
#       print(score)
# printScores("Jonathan",100, 95, 88, 92, 99)

# def printThese(a=None,b=None,c=None):
#    print(a, "is stored in a")
#    print(b, "is stored in b")
#    print(c, "is stored in c")
# printThese(c=3, a=1)

# def printThese(a,b,c=None):
#    print(a, "is stored in a")
#    print(b, "is stored in b")
#    print(c, "is stored in c")
# printThese(1,2)
# a = [1,2,3]
# b = [*a,4,5,6]
# print(b) # [1,2,3,4,5,6]
# def printPetNames(owner, **pets):
#    print(f"Owner Name: {owner}")
#    for pet,name in pets.items():
#       print(f"{pet}: {name}")
# printPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")

# def sum():
#     x = 10
#     x = x + 5
#     print(x)
# sum()

# x = 10
# def sum():
#     x = 11
#     x = x + 5
#     print(x)
    
# sum()
# print(x)

# x = 10
# def sum():
#     global x
#     x = x + 5
#     # выводим сумму с глобальной переменной = 15
#     print(x)
    
# sum()
# # выводим значение глобальной переменной
# # оно поменялось и равно 15
# print(x)
# """Циклы - for, while"""
# lst=[45,875,78,879,12,5,9]
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# print(lst[4])
# print(lst[5])
# print(lst[6])
# print("""""")
# for i in range(len(lst)):
#    print(lst[i])

# for i in range(2,len(lst)):
#    print(lst[i])
   
# for i in range(len(lst)):
#    print(lst[2])   
# for i in lst:
#    print(i)  
# ls=[]
# for i in lst:
#    if i % 2 != 0:
#       print(i)
#       ls.append(i)
# print(ls)

# while True:
# students=[]
# for i in range(7):
#    name=input("Введите имя студента: ")
#    students.append(name) 
# print(students)
# name2=input("ВВедите имя студента: ")
# if name2 in students:
#    print(name2,"да есть это наш студент")
# else:
#    print("не наш студент")

# ls=''
# num=int(input("Введите число: "))
# for i in range(num+1):
#    for y in range(i):
#       ls = (str(i) + ' ')*i 
#    print(ls)      
# i = 5
# while i < 15:
#   print(i)
#   i = i + 2
# for i in 'hello world':
#     if i == 'a':
#        break
# else:
#    print('Буквы a в строке нет')
   
# a=input("Введите слова: ")
# a=a.split(".")
# b=''
# b=b+a[1]+"."+a[0]
# print(b)
# my_lst = [1, 5, 6, 1, 8, 4, 4, 5, 1]
# dict={}
# for i in my_lst:
#    if my_lst.count[i]<1:
#       dict.append=my_lst[i]
# print(dict) 
