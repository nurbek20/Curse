# x = [4, 7, 8, 24, 12, 2, 1,58,-4]

# def find_max(x):
#     max_num=x[0]
#     for i in x:
#         if max_num<i:
#             max_num=i
#     print(max_num)
# find_max(x)

# lst1=[1,5,8]
# sum=0
# count=0
# for i in lst1:
#     sum=sum+i
#     count = count + 1
#     # sum = sum / 3

# print("Сумма всех числел: ",sum)
# print("Количества всех чисел: ",count)
# print("Среднее ариф. значения: ",sum/count)
 

# def find_midd(lst1):
#     summ=0
#     count=0
#     for i in lst1:
#         summ=summ+i
#         count=count+1
#     print(summ/count)
# find_midd(lst1)
# f=[4,4,2]
# def find_midd(l):
#     summ=0
#     count=0
#     for i in l:
#         summ=summ+i
#         count=count+1
#     return summ / count
# print(find_midd(f))        

# a='Hello'
# count=0
# for i in a:
#     if i=="l":
#         count = count + 1
# print(count)
# season=int(input("Введите номер месяца: "))
# if 0 < season < 4:
#     print ("Зима") 
# elif 3 < season < 7:
#     print ("Весна") 
# elif 6 < season < 9:
#     print ("Лето") 
# elif 8 < season < 13:
#     print ("Осень") 
# else:
#     print('ERROR')

# fruits=["банан","яблоко","ананас","банан","груша","банан"]
# del_fruit=input("Введите названия фрукта для удаления: ")
# add_fruit=input("Введите названия фрукта чтобы добавить в список: ")
# # fruits1=[]
# s=0
# for i in fruits:
#     if i == "банан":
#         print(i)

# fruits.remove(del_fruit)
# fruits.append(add_fruit)
# print(fruits) 
# 
#        
#Problem1
# Написать Функцию которая принимает предложение как аргумент, считает
# количество букв и возвращает сколько символов он ввёл. НЕ ИСПОЛЬЗОВАТЬ

# def my_txt(txt):
#     summ=0
#     txt=txt.replace(" ","")
#     for i in txt:
#         summ += 1
#     print(summ)
# my_txt("apple macv")
# fuzz=5
# def mySum(a,b):
#     return a + b
# print(mySum(5,6))  

# for i in range(1100,4600):
#     if i % 4==0 and i % 5 !=0:
#         print(i)
      


# course="itcbootcomp"
# d={}
# count=0
# for i in course:
#     if i == "i":
#        count += 1
# d["i"]=count                
# print(count)
# print(d)

# for i in course:
#     if i == "t":
#        count += 1
# d["t"]=count
# print(d)

# for i in course:
#     if i == "c":
#        count += 1
# d["c"]=count
# print(d)

# for i in course:
#     if i == "b":
#        count += 1
# d["b"]=count
# print(d)

# for i in course:
#     if i == "o":
#        count += 1
# d["o"]=count
# print(d)

# for i in course:
#     if i == "t":
#        count += 1
# d["t"]=count
# print(d)

# for i in course:
#     if i == "m":
#        count += 1
# d["m"]=count
# print(d)

# for i in course:
#     if i == "p":
#        count += 1
# d["p"]=count
# print(d)

# def mult_numbers(l):
#     mult=1
#     for i in l:
#         mult *= i
#     return mult
# print(mult_numbers([45,1,2,5,8])) 
# a=[i for i in "itcbootcamp" ]
# print(a)       

