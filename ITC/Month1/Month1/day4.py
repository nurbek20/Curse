# print("Hello World:")
# print(type("Hello World:")) #str

# # """
# # from typing import Tuple
# # Типы данных:
# # str         Например: "Python developer"
# # int         Например: 123, 56, 985321, 54
# # float       Например: 2.5, 14.2, 3.5
# # list        Например: [45, 'Text', 'python'
# # Dictionary  Например: {4:"class", "book":"web Development"}
# # set         Например: {12, 5, 'good', True}
# # Tuple       Например: (54, 74, 'computer')
# # Boolean     Например: True, False
# # """
# # """склеивания строк"""
# my_str="My name Nurbek"
# mult_str=""" """
# my_str2='Python Develooper'      #str
# my_str3="Python Develooper"      #str
# my_str4='''Python Develooper'''  #str
# my_str5="""Python Develooper"""  #str

# text2="Жанна д'Арк'"
# print("text2")

# print(my_str)
# print(mult_str)
# name="Anna"
# last_name="Alexy"
# age=25
# print(name+last_name)  
# print(name+" "+last_name)
# print(name+" is "+str(age)+"y.o")

# name="My name is Meerim, "
# age="I am 20 y,o"
# print(name+"\n"+age)          #\n -перенос строки 

# # """ Фрифметичкская операция"""
# fistNum=5
# secondNum=4
# fistNum1="5"
# secondNum2="4"

# print(fistNum+secondNum)  #9 ->int
# print(fistNum1+secondNum2)   #54 ->str
# summ=fistNum+secondNum
# print=(summ) #9
# print(type(sum)) #int

# summ2=fistNum1+secondNum2
# print(summ) #54
# print(type(summ)) #str

# a=89
# b=54
# c=143
# print(a, "+", b, "=", a+b)
# print(str(a)+"+"+str(b)+"="+str(c))


# print(a,"-",b,"=",a-b)
# print(a,"*",b,"=",a*b)
# print(a,"/",b,"=",a/b)

# fnum=int(input("Введите первое число:")) 
# snum=int(input("Введите второе число:"))  
# print(fnum,"+",snum,"=",fnum+snum)
# print(fnum,"*",snum,"=",fnum*snum)
# print(fnum,"-",snum,"=",fnum-snum)
# print(fnum,"/",snum,"=",fnum/snum)


# """форматьирования строк"""
name=input("Введите ваше имя: ")
age=input("Введите ваш возраст: ")
number=float(input('Введите ваш номер: '))
print("имя: ",name, age, 'лет' ,number)
print("{0} {1} лет  номер {2}".format(name, age, number))
# print("{1} {0} лет".format(name, age))
# print("{n} {a} лет".format(n=name, a=age))

# print(f"{name} {age} лет")
# print(f"{age} {name} лет")
