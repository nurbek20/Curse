# number= int(input("Введите число: "))
# for i in range(1,11):
    # print(f"{number} * {i} = {number*i}")
    # print(i,"*", number,"=", i*number)
    # print(str(i)+"*"+str(number)+"="+str(i*number))
    # print("{0}*{1}={2}".format(i,number,i*number))    

# list1=[10,20,30,40,50]
# lst=[]
# for i in range(1,len(list1)+1):
#     lst.append(list1[-i])
# print(lst)
# i=1
# while i < len(list1):
#     lst.append(list1[i])
#     i = i + 1
# print(lst)    

# """Двухмерные массивы"""
# my_lst=[45,87,789,44]
# my_lst2=[
#           [45,78,45,12],
#           [5,787,78,15],
#           [8,2,45,877]
# ]
# print(my_lst2[0][0])
# print("Количечтва всех элементов: ",len(my_lst2))
# # print(len(my_lst2[0])+len(my_lst2[1])+len(my_lst2[2]))
# c=0
# for i in range(len(my_lst2)):
    # if i % 2 ==0:
        # c = i + 1
        # c = i + 1
    # print(len(my_lst2[i])) 
#     c=c+len(my_lst2[i])
#     print(c)
# summ=0     
# for i in  range(len(my_lst2)):
#     for y in range(len(my_lst2)):
#         print(my_lst2[i][y]) 
#         summ = summ+my_lst2[i][y]
# print(summ)
# my_lst3=[
#           [45,-78,-45,12],
#           [5,-787,78,15],
#           [8,2,45,877]
#           ]
# lst = [
#     [10,-20,34],
#     [23,50,-45],
#     [-45,32,-23]
#     ]
# lst1=[]
# for i in range(len(lst)):
#     for y in range(len(lst)):
#         if lst[i][y]<0:
#             lst1.append(lst[i][y])
# print(lst1)
# for i in range(len(my_lst3)):
#     for y in range(len(my_lst3)):
#         if my_lst3[i][y]< 0:
#             print(my_lst3[i][y])
# c=0
# summ=0
# for i in range(len(my_lst3)):
#     for y in range(len(my_lst3[i])):
#         if my_lst3[i][y]<0:
#             c =c+1
#             summ=summ+my_lst3[i][y]
# print(c)    
# print(summ)

#  """Function - Функция"""
# print("text")
# def my_function():
#     print("My_function")
# my_function()
# my_function()
# my_function()

# my_sum() a=5 b=7 =>12
# my_sub() a=5 b=7 =>-2
# my_mult() a=5 b=7 =>35
# my_div() a=5 b=7 =>0.....

# def my_sum():
#     a=5
#     b=7
#     print(a+b)
# my_sum() 

# def my_sub():
#     a=5
#     b=7
#     print(a-b)
# my_sub()    
# def my_mult():
#     a=5
#     b=7
#     print(a*b)
# my_mult()    
# def my_div():
#     a=5
#     b=7
#     print(a/b)
# my_div()  

# def my_sum2():
#     a=2
#     b=4
#     c=a+b
#     # print(c)
#     return c
# print(my_sum2()) 
# def sum_of_digit(a,b,c):
#     print(a+b+c)
# sum_of_digit(5,6,9)
# def func(num):
#     ls=[]
#     for i in range(num):
#            ls.append(i)
#     print(ls)
# func(5)    
# def func(num):
#     ls=[]
#     for i in range(num):
#         if i %2==0:
#            ls.append(i)
#     print(ls)
# func(9)
# def func(num):
#     ls=[]
#     i=1
#     for i in range(num):
#         # if i >0:
#         ls.append(i)
#         # ls = ls + 1
#     print(ls[::-1])
# func(7)
# def my_title(txt):
#     print(txt.title())
# a=input("Введите тектс: ")
# my_title(a)
# def my_title(txt):
#     print(txt.upper())
# a=input("Введите тектс: ")
# my_title(a)
# def my_title(txt):
#     print(len(txt.split()))
# a=input("Введите тектс: ")
# my_title(a)
# my_lst3=[
#           [45,-78,-45,12],
#           [5,-787,78,15],
#           [8,2,45,877]
#           ] 

# def my_ls():
#     max_num=0
#     for i in range(len(my_lst3)):
#         for y in range(len(my_lst3[i])):
#             if my_lst3[i][y]>0:
#                 max_num=my_lst3[i][y]
#     print(max_num)
# my_ls()    

# def my_ls():
#     max_num=0
#     for i in range(len(my_lst3)):
#         for y in range(len(my_lst3[i])):
#             if my_lst3[i][y]<0:
#                 max_num=my_lst3[i][y]
#     print(max_num)
# my_ls()    

