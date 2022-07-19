# #""" Циклы, for. while"""
# for i in range(1,10):
#     if i ==5:
#         print(i)
#     else:
#         print("неизвесний номер")

# lst=[1,3,5,7]
# count=0
# for x in lst:           #1) x=1                   2)x=3        3)x=5          4)x=7
#     count=count+x        # count=0+1=>1          count=1+3=>4    count=4+5=>9  count=5+7=>16
#     #count += x
# print(count)


# lst2=[12,8,54,45,987,5]
# count=0
# for i in lst2:
#     if i % 2==0:
#         count += i
#         #count=count+i
# print(count)
# print(sum(lst2))

# number=int(input("Введите число:"))
# for i in range(1,10):
#     print(f"{number} + {i} =",i+number)
 
# lst3 = [2,5,1,3]
# s=1
# for i in lst3:
#     s = s* i
# # print(s)
# c=1
# for i in range(1,31):
#     if i %3 ==0 and i%5==0:    
#             c = c*i
#             print("Число которые делятся на без остатка 3 и на 5 ",i)
# print(c)        

# c=1
# col=0
# for i in range(6,64):
#     if i %2==0 or i%3==0:
#         c += i
#         col = col + 1
#         print("Число которые делятся на без остатка 2 и на 3",i)
# print(c) 
# print("Число которые делятся на без остатка 2 и на 3", col)

#     """while"""   
# my_lst=[1,2,3,4]
# for i in my_lst:
#     print(i)
# for i in range(len(my_lst)):   for i in range(4)  => 0,1,2,3
#     print(my_lst(i))

# i=0            #i>=4
# while i < len(my_lst):      #до 0<4=> True    до  1<4=> True   2<4   3<4   4<4  True
#     print(my_lst[i])         # 1                 2      3       4
#     i = i + i                    # i = 0 + 1   i=1+1   i=2+1  i=3+1
# my_lst=[1,2,3,4]
# i=0
# sum1=0
# col=0
# p=1
# while i < len(my_lst):
#     sum = sum1 + my_lst[i]
#     col = col+1
#     i = i + 1
#     # p *= i
# print("Сумма:",sum1)
# print("Кол-во:",col)
# print("Произведения", p)
# l=[5,78,-6,8,-45]
# l2=[]
# l3=[]
# i=0
# while i < len(l):
#     if l[i]>0:        
#        # print(l[i])
#         l2.append(l[i])
#     else:    
#         l3.append(l[i])   
#     i += 1 
# print(l2) 
# print(l3)    
#while i < len (l):


# i=1
# while i <100:
#     print(i)
    # i = i + 2
# for i in range(1, 100, 2):
#     print(i)
# while i > 100:
#     print(i)
#     i = i + 2

# i=0
# while i < 100:
#     if i % 2!=0:
#         print(i)
#     i = i + 1    