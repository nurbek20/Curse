# 1)
# Напишите функцию Python для вычисления факториала числа 
# (неотрицательное целое число). Функция принимает число в качестве аргумента.
# n = int(input("Введите число: "))
# factorial = 1
# for i in range(2, n+1):
#     factorial *= i
# print(factorial)


# 2)
# Создайте рекурсивную функцию Напишите программу для создания
#  рекурсивной функции для вычисления суммы чисел от 0 до 10.
#  Рекурсивная функция - это функция, которая вызывает себя снова и снова.
# def recurs(res):
#     for i in range(1, 10):
#         res *= i
#     print(res)
#     recurs(res)
# recurs(9)

def a(num):
    if num:
        return num + a(num-1)
    else:
        return 0
res=a(10)
print(res)        


# 3)
# Назначьте другое имя функции и вызовите ее через новое имя 
# Ниже представлена ​​функция display_student (имя, возраст).
#  Присвойте ему новое имя show_tudent (имя, возраст) и назовите его новым именем.

# def display_student(name, age):
#     print(name, age)

# show_tudent = display_student

# show_tudent("Nurbek", 26)

# 4)
# Сгенерируйте 3 случайных целых числа от 100 до 999, которые делятся на 5

# import random
# num1=random.randint(3)

# for i in range(3):
#     if i % 5 == 0:
#         print(random.randint(100,999))   
#     print(i%random.randint(100,999))


# lst = []
# while len(lst) < 3:
#     i = random.randint(100, 999)
#     if i % 5 == 0:
#         lst.append(i)
# print(lst)




# def random5_7():
#     num = random.randint(100,999)
#     if num % 5 == 0:
#         return num
#     else:
#         return random5_7()
# print(random5_7())            