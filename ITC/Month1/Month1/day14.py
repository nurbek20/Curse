#  4. С помощью while у человека имя фамилию и отчество:
#  Проси до тех пор пока человек не вводит свои данные
# name=input("Введите ваше Ф И О: ")
# name="Anna"
# l_name="Kirillovskaya"
# n=input("Введите ваше имя: ")
# l=input("Введите вашу фамилию: ")
# while name != n or l_name != l:
#     n=input("Введите ваше имя: ")
#     l=input("Введите вашу фамилию: ")
 # 6. Найти все число делящееся на 7 без остатка из ряда чисел от 7 до 457
#  и вывести на экран, иcпользуя while   
# c=1
# for i in range(7,457):
#     if i % 7 == 0:
#             c = c + i
#             print("число которые делятся 7 без остатка",i)
# i=7
# while i < 457:
#     if i % 7 == 0:
#         print("число которые делятся 7 без остатка",i)
#     i = i + 1    

# numbers = [67, 99, 56, 43, 66, 12]
# count=0
# for i in range(len(numbers)):
#     count += numbers[i]
#     print(count)
# print(count)

# count=0
# i=0 
# while i < len(numbers):
#     count= count + numbers[i]
#     i = i + 1

# print(count)    
# while True:
    # print("бесконечный цикл")
# i = 0
# while True:
#     if i ==20:
#         break
#     else:
#         print(i) 
#         i = i + 1  

# my_dict={"name":"Nurbek", "gender":"man","profession":"web develooper" }
# my_dict["city"]="Osh"
# key= input("Введите ключ словаря: ")
# value= input("Введите значения словаря: ")
# my_dict[key]=value
# print(my_dict)

# for i in  my_dict:
#     print(i)       # получить только ключи


# for i in  my_dict:
#     print(i, "-" ,my_dict[i])       
#     print(f"{i} - {my_dict[i]}")
# for key, value in my_dict.items():
#     print(key,"-", value)

# for key in my_dict.keys():
#     print(key)

# for i in my_dict.values():
# #     print(i) 
# words1={}
# words=["black","черный","white","белый","blue","синий"]
#
#  for i in range(len(words)):
#     if i % 2 == 0:
#         words1[words[i]]=words[i+1]
# print(words1) 
# words2=[]
# for i in words1:
#     words2.append(i)

#     words2.append(words1[i])
    
# print(words2)
# dct={5:"five", 4:"four", 3:"three", 0:"zero", 2:"two",1:"one"}
# i=0
# for i in dct:
#     # print(i,dct[i])
#     if i ==0:
#         break
#     else:
#         print(i,dct[i])
        # i + i + 1

# my_list=[1,5,6,1,8,4,4,5,1]
# n=int(input("Введите число: "))
# my_list1={}
# c=0
# for i in my_list:
#     if i == 5:
#      c = c + i     
#      n = n + i 
#      print(c, n)