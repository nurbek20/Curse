# a = input('Введите число: ')
# l=[]
# for i in range(len(a)):
#     if a[i] != a[-1]:
#         if a[i] <= a[i+1]:
#             print(a ,'False')
#             l.append(a)
#             print(*l,'False')
#             break
#         else:
#             print(a, 'True')
#             l.append(a)
#             print(*l,'True')
#             break

# n=5
# ls=''
# for i in range(n):
#     for y in range(i):
#         ls = (str(i) + ' ') * i
#     print(ls)

# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print("{0}={1}".format(key, value))
#     greet_me(name="yasoob")
# name=yasoob
# def test_args_kwargs(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
# args=("two", 3, 5)
# test_args_kwargs(*args)
# kwargs={"arg3": 3, "arg2": "two", "arg1": 5}
# test_args_kwargs(**kwargs)

# some_func(farg, *args, **kwargs)
# import  someclass
# def get_info(self, *args):
#     return "Test data"
# someclass.get_info = get_info
# class Factory:
#     def engine(self):
#         print("Двигател создан")
#     def bridge(self):
#         print("Ходовая часть создана")
# class Toyota(Factory):
#     def wheels(self):
#         print("Калеса готовы")
#     def windows(self):
#         print("Стекло готовы")
# car=Toyota()
# car.engine()
# car.bridge()
# car.wheels()
# car.windows()
# print(17 % 5)
# print(10+ int('20'))

# nums=[8, 1, 2, 2, 3]
# lst=[]
# for i in range(len(nums)):
#     count1=[]
#     for j in range(len(nums)):
#         if nums[i]>nums[j]:
#             count1.append(nums[j])
#             lst.append(len(count1))
# print(lst)
# l=sorted(nums)
# r=[]
# for i in range(len(nums)):
#     r.append(l.index(nums[i]))
# print(r)
# nums = [1,2,1]
# print(nums*2)
# n=nums[::]
# n=[]
# for i in nums:
#     n.append(i)
# print(n)
# words=["a"]

# n=['a':".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# words = ["gin","zen","gig","msg"]
# n = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
# old = []
# t = 0
# while t < len(words):
#     one = []
#     for i in words[t]:
#         one.append(n[i])
#     old.append(''.join(one))
#     one = []
#     t+=1
# new = []
# for i in old:
#     if i not in new:
#         new.append(i)
#     return len(new)


# nums = [5, 4, 2, 1, 0, 3]
# res = [nums[0], nums[nums[1]], nums[nums[1]] , nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
# res = [nums[5], nums[4], nums[2], nums[1], nums[0], nums[3]]
# res = [3, 0, 2, 4, 5, 1]

# print(len(nums))
# new=[]
# for i in range(len(nums)):
#     new.append(nums[nums[i]])
# print(new)

# nums=[1, 2, 3, 4]

# for i in range(1, len(nums)):
#     nums[i] += nums[i-1]
# print(nums)
# accounts = [[1,2,3],[3,2,1]]
# # print(accounts+accounts)


# sums = [sum(i) for i in accounts]
# sums.sort()
# print(sums[-1])

# a= "1,2,3,4,5,6"

# print(a.replace(",", "[,]"))

#  sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

# class Solution(object):
#     def mostWordsFound(self, sentences):
#         """
#         :type sentences: List[str]
#         :rtype: int
#         """
#         result = []
#         for element in sentences:
#             result.append(len(element.split()))
#             result.sort()
#         print(result[-1])
# n=Solution()
# n.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])

# import instaloader
# Profile =input ("Введите ваш аккаунть ")
# insta=instaloader.instaloader()
# insta.download_profile(profile_pic_only=True)
# foo = [2,17,9,22,17,24,8,11,27]
# foo = [x for x in foo[::2] if x % 2 == 0 ]
# print(foo)
# print(4+5)

# print(2**3 - 4)

# l=[]
# for i in range(7,453):
#     if i %7==0:
#         l.append(i)
# print(l)
# n=[]
# for i in range(7,453,7):
#     n.append(i)
# print(n)
# arr = [10, 37, 29, 77, 50, 20, 21, 77, 26, 50, 84]
# summa = 0
# for x in arr:
#     summa += x
# print(summa)

# print(5==6)


# print(num<18)
# while True:
#     num = int(input("введите ваш возрасть: "))
#     if num<18:
#         print("вам меньше 18 лет")
#     elif num>18:
#         print("Вам больше 18 лет")
#     elif num==18:
#         print("Вам 18 лет")

# lst = [
#     [23,54,23,534],
#     [23,54,23,564],
#     [23,54,23,53],
# ]
# l=0
# for i in lst:
#     for y in  i:
#         l += 1
# print(l)


# Nurseit Faruh

# person = {"name": "Nurseit", "money": 20000, "pass": "2006"}
# old_password = [2006]
# password1 = [2006]
# for i in range(3):
#     # name = int(input('Введите имя:'))
#     password = int(input('Введите свой пароль:'))
#     if password in password1:
#         print('найдено')
#         print('Пожалуйста, введите варианты, которые вы хотите сделать:')
#         break
#     elif i == 2:
#         print('попытки не остались')
#         break
#     else:
#         print('не найдено')
#         print('попробуйте еще раз')
# while 1:
#     print("нажмите money, что бы проверить баланс\nнажмите add, что бы пополнить баланс\nнажмите take off,что бы снять деньги\nнажмите change password,что бы сменить пароль\nнажмите exit,что бы выйти из бонкамата")
#     key = input()
#     if key == "money":
#         print("your money : {}".format(person["money"]))
#     if key == "add":
#         money = int(input("Сколько вы хотите добавить?>"))
#         person["money"] = person["money"] + money
#     if key == "take off":
#         money = int(input("Сколько вы хотите снять?>"))
#         person["money"] = person["money"] - money
#     if key == "change password":
#         money = int(input("Введите старую пароль?"))
#         if money in old_password:
#             print('найдено')
#             money1 = input("Введите новую пароль?")
#             money2 = len(money1)
#             if money2 == 4:
#                 print('пароль изменен')
#                 break
#             elif i == 3:
#                 print('попытки не остались')
#                 break
#             else:
#                 print('напишите 4 число')
#         elif i == 3:
#             print('попытки не остались')
#             break
#         else:
#             print('не найдено')
#             print('попробуйте еще раз')
#     if key == 'exit':
#         break


# Asadbek Daniel

# pin = [1234]
# balans = [2000]
# SOM = ('Сом')
# USD = ('Доллар')
# KZT = ('Тенге')
# RUB = ('Рубль')
# EVRO = ('Евро')
# while True:
#     kod = int(input('Введите код: '))
#     if kod in pin:
#         print('Добро пожаловать')
#         step2 = str(input('Что вы хотите зделать?: '))
#         if step2 == 'Снять деньги':
#             volute = str(input('Выберите валюту: '))
#             if volute in SOM:
#                 lowmoney = int(input('Введите сумму: '))
#                 if lowmoney >= 2000:
#                     print('Вваш баланс менее', *balans)
#                     break
#                 elif lowmoney <= 2000:
#                     print('Выдано', *balans)
#             elif volute in USD:
#                 lowmoney = int(input('Введите сумму: '))
#                 print('Снято ', lowmoney, USD)
#                 if lowmoney >= 2000:
#                     print('Вваш баланс менее', *balans)
#                     break
#                 elif lowmoney <= 2000:
#                     print('Выдано', *balans)
#             elif volute in KZT:
#                 lowmoney = int(input('Введите сумму: '))
#                 print('Снято ', lowmoney, KZT)
#                 if lowmoney >= 2000:
#                     print('Вваш баланс менее', *balans)
#                     break
#                 elif lowmoney <= 2000:
#                     print('Выдано', *balans)
#             elif volute in RUB:
#                 lowmoney = int(input('Введите сумму: '))
#                 print('Снято ', lowmoney, RUB)
#                 if lowmoney >= 2000:
#                     print('Вваш баланс менее', *balans)
#                     break
#                 elif lowmoney <= 2000:
#                     print('Выдано', *balans)
#             elif volute in EVRO:
#                 lowmoney = int(input('Введите сумму: '))
#                 print('Выдано ', lowmoney, EVRO)
#                 if lowmoney >= 2000:
#                     print('Вваш баланс менее', *balans)
#                     break
#                 elif lowmoney <= 2000:
#                     print('Выдано', *balans)
#             else:
#                 print('Недостаточно средств')
#                 break
#         elif step2 == 'Проверить баланс':
#             volute = str(input('Выберите валюту: '))
#             if volute in SOM:
#                 print('Ваш баланс составляет', *balans, SOM)
#             elif volute in USD:
#                 print('Ваш баланс составляет', *balans, USD)
#             elif volute in KZT:
#                 print('Ваш баланс составляет', *balans, KZT)
#             elif volute in RUB:
#                 print('Ваш баланс составляет', *balans, RUB)
#             elif volute in EVRO:
#                 print('Ваш баланс составляет', *balans, EVRO)
#             else:
#                 print('Выход')
#         elif step2 == 'Положить деньги':
#             volute = str(input('Выберите валюту: '))
#             if volute in SOM:
#                 inbank = int(input('Введите сумму: '))
#                 print('Добавлено на баланс ', inbank, SOM)
#                 break
#             elif volute in USD:
#                 inbank = int(input('Введите сумму: '))
#                 print('Добавлено на баланс ', inbank, USD)
#                 break
#             elif volute in KZT:
#                 inbank = int(input('Введите сумму: '))
#                 print('Добавлено на баланс ', inbank, KZT)
#                 break
#             elif volute in RUB:
#                 inbank = int(input('Введите сумму: '))
#                 print('Добаывлено на баланс  ', inbank, RUB)
#                 break
#             elif volute in EVRO:
#                 inbank = int(input('Введите сумму: '))
#                 print('Добаывлено на баланс  ', inbank, EVRO)
#             else:
#                 print('Выход')
#     else:
#         print('Error')


# Saipudin Husan

# a=input('Введите пароль: ')
# password = 'itc'

# тил = 'Kgz'
# язык = 'Rus'
# language = 'USA'

# som = 'KGZ'
# rubl = 'RU'
# dollar = 'USD'

# меню = 'снять деньги', 'проверка баланс','пополнит баланс','перевод деньги'
# тандоо = 'накталай алуу', 'балансты текшеруу','балансты толуктоо','акча которуу'
# menu = 'withdraw money', 'balance check','replenish the balance','money transfer'

# v = 'снять деньги'
# c = 'проверка баланс'
# d = 'пополнит баланс'
# e = 'перевод деньги'

# if a == password:
#     print('пароль верно')
#     b = input('Выберите язык: ')
#     if b == язык:
#         print(меню)
#         m = input('Выберите пункт: ')
#         if m == v:
#             k = input('Выбор валюта: ')
#             if k == rubl:
#                 input('Введите сумму: ')
#         m1 = input('Выберите пункт: ')
#         if m == v:
#             k = input('Выбор валюта: ')

# elif a != password:
#     print('пароль не правильно')