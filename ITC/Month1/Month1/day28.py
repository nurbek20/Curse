# """open()"""
# # r   для читения файла
# # w   записать файл
# # a   дабавить запись в конце 
# # x   создать файл
# # создать файл
# # my_file = open("my_file.txt","x")

# # записать файл
# my_file2 = open("new_file.txt","w")
# my_file2.write("Hello world!!!")
# my_file2.close()
# # дабавить запись в конце
# my_file3 = open("new_file.txt","a")
# my_file3.write("\nHello everybody\n")
# my_file3.close()

# my_file4 = open("new_file.txt","a")
# my_file4.write("Python\n")
# my_file4.close()


# my_file6 = open("new_file.txt","a+")     # для записи и чтения
# my_file6.write("New words")
# my_file6.read()
# my_file6.close()

# my_file5 = open("new_file.txt","r")
# # print(my_file5.read())
# # for i in my_file5:
# #     print(i,"good")

# m = my_file5.readlines()
# print(m)  
# print(type(m))
# count=0
# c = 0
# for i in m:
#     for y in i:
#         if y.lower() == "h":
#             count += 1
#         elif y == "y":
#             c += 1    
# print("h: ", count)
# print("y: ",c)

# создать файл
# my_file = open("my_file.txt","x")

# # исключения 
# file_name = input("Напишите названия файла для создания: ")
# try:
#    new  = open(file_name,"x")
#    print("файл создан")
# except FileExistsError:
#     print("Такой файл уже существует!!!")
# finally:
    # new.close()
# a = int(input("Введите число: "))
# b = int(input("Введите второе число: "))
# try:
#     print("Резултать", a / b)
# except ZeroDivisionError:
#     print("На ноль делить нельзя") 
# o = open("new_file.txt","w", encoding="UTF-8")
# o.write("Всем привет!!! \n")
# o.write("Всем привет!!!")
# o.close()
# o2 = open("new_file.txt","r")
# # print(o2.read())
# # print(o2.readlines())   # list
# # print(o2.readline(1))    # str
# print(o2.read(4))
# import os

# os.remove("s")            # remove file
# os.rmdir("nnnnnnnnnn")    # remove directory

# os.mkdir("myy")             # создать папка
# import os
# u=int(input("Для создания введите 1:\nДля записи введите 2:\nДля 
# тение введите 3:\nДля добавление введите 4:\nДля добавления и чтения введите 5
# :\nДля удаления файла введите 6:\nЕсли хотите создать папку введите 7:\nЕсли хотите
#  удалить папку введите 8:"))
# if u == 1:
#     file_name=input("Напишите название файла для создания:")
#     try:
#         new = open(file_name, "x")
#         print("Файл создан")
#     except FileExistsError:
#         print("Такой файл уже создана")
# elif u == 2:
#     f=input("Что хотите:")
#     my_file2= open("new_file", "w")
#     my_file2.write(f"{f}\n")
#     my_file2.close()
# elif u == 3:
#     my_file5= open("new_file","r")
#     print(my_file5.read())

#             elif u == 4:
#                         o=input("Что хотите:")
#                         my_file3 = open("new_file", "a")
#                         my_file3.write(f"{o}")
#             my_file3.close
# elif u == 5:
#     d=input("Что хотите:")
#     my_file6=open("my_file.txt","a+")
#     my_file6.write(f"{d}")
#     my_file6.read()
#     my_file6.close()
# elif u==6:
#     try:
#         q=input("Какой файл хотите удалить:")
#         os.remove(q)
#     except FileNotFoundError:
#         print("Такого файла не существует")
# elif u==7:
#     h=input("Название папки:")
#     os.mkdir(h)             # создать папку
# elif u==8:
#     try:
#         e=input("Какую папку хотите удалить:")
#         os.rmdir(e)
#     except FileNotFoundError:
#         print("Такой папки не существует")
#     else:
#         print("В:ведите толко цифры до 8!!!")

import os
while True:
    name=int(input("""Если хотите создать файл введите 1:
Если хотите запис напишите 2:
Если хотите читать файл ведите 3: 
Если хотите добавить  введите 4:
Если хотите добавить и читать введите 5:
Если хотите удалить файла введите 6:
Если хотите создать папки введите 7:
Если хотите удалить папки введите 8:
Для выхода введите 9: """))
    if name == 9:
        quit()
    try:
        if name == 1: 
            n=input("пишите называния файла: ") 
            new  = open(n+'.txt',"x")
            print("файл создан")    
    except FileExistsError:   
            print("Такой файл уже существует!!!") 
    if name == 2:
            n1=input("выберите файла для записи: ")
            
            new = open(n1+'.txt',"w")     
            new.write(input("Введите текст для записи: "))
            new.close()
    if name == 3:
            new = open(n1+'.txt','r')
            print("Соддержиммое в файле: ",new.read())
            new.close()
    elif name == 4:
            n1=input("выберите файла для записи: ")
            new = open(n1+'.txt',"a+")
            new.write(input("Введите текст для записи: "))
            new.close()
    elif name == 5:
            n1=input("выберите файла для записи: ")
            new = open(n1+'.txt',"a+")
            new.write(input("Введите текст для записи: "))
            new = open(n1+'.txt',"r")
            print('Соддержимое в файле: ',new.read()) 
            new.close()
    elif name == 6:
        try:
            n2=input("Какой файл хотите удалить:  ")
            os.remove(n2)
            print("файл удален")
        except FileNotFoundError:
            print("Такого файла не существует")
    elif name == 7:
        name1=input("Введите называния папки: ") 
        os.mkdir(name1)   
    elif name == 8:
        try:
            n3=input("Какую папку хотите удалить: ")
            os.rmdir(n3)
            print("папка удален")
        except FileNotFoundError:
            print("Такой папки не существует")