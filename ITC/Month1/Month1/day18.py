# # """Встроенные библиотека"""
# # """random()"""    случайные число
import random
# num1 = random.randint(0, 50)
# print(num1)

# for i in range(6):
#     print(random.randint(0,100))    # int

# for i in range(8):
#     print(10)
# f=random.random()                   # float
# print(f)
# угадай число(0,20)
randnum=random.randint(0,20)       # 8
while True: 
    # print(randnum,True)
    num = int(input("Угадайте число: "))
    if num > randnum : 
        print("ваше число больше моего ")
    elif num < randnum:
        print("ваше число меньше моего")
    elif num == randnum:
        print("да верно, вы нашли")
        break
    else:
        print('Неверная команда!!!')
        break

# course="itcbootcamp"
# print(course[random.randint(0, len(course))])    

# """choice"""
# print(random.choice(course))
# python="The official home of the Python Programming Language".replace(" ","")
# n=random.choice(python)
# count=0
# for i in python:
#     if i==n:
#         count+=1
# print(f"{n} повторяется {count} раз.")
# # """datetime"""
# import datetime
# from datetime import date, time

# today = datetime.datetime(2021, 12, 2, 16 ,42, 25)
# my_date=date(2009, 8, 27)
# my_time=time(16, 45, 26)
# print(today)
# print(my_date)
# print(my_time)

# today2=datetime.datetime.today()
# print(today2)
# now2=datetime.datetime.now()
# print(now2)
# print(now2.year)  #год
# print(now2.month) #месяц
# print(now2.day)   #день
# print(now2.hour)   #час
# print(now2.minute)  #минута
# print(now2.second)   # секунда

# now22=datetime.datetime.now().weekday()
# print(now22)

# print(today.strftime("Дата: %y-%m-%d"))    # Дата: 21-12-02
# print(today.strftime("Дата: %y-%m-%d"))    # Дата: 21-12-02
# print(today.strftime("Дата: %d-%m-%y"))    # Дата: 02-12-21
# print(today.strftime("Время: %H-%M-%S"))   # Время: 16-42-25