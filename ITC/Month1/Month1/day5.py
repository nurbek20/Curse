# ***Методы str***

text="I live in osh"
print(text)
print(text.replace("o","O"))

# a="()блак()"
# print(a)
# print(a.replace("()","o"))
# b="м{}л{}[]{}"
# print(b.replace("{}","о").replace("[]","к"))
# new_b=b.replace("{}","о")


# # """метод .title()"""
# country="кыргызская республика"
# print(country)
# print(country.title)

# str1="к т р к"
# str2="э л т р"
# print(str1.title().replace(" ",""))
# print(str2.title().replace(" ",""))


# # """Метод, upper()"""

# str1="ктрк"
# print(str1)
# print(str1.upper())    #КТРК
# print(str1.title())    #Ктрк

# #     """Метод .lower()"""
# str3="КТРК"
# print(str3)           #КТРК
# print(str3.lower())   #ктрк

# str4="Ош"
# print(str4.lower())    #ош

# str5="Жанна д'Арк"
# print(str5.lower())    #жанна д арк

# city1="иссык куль"
# city2="КарА бАлта"
# print(city1.title().replace(" ", "-"))
# print(city2.lower().title().replace(" ","-"))

# # """Метод len()"""
# my="Kyrgyzstan"
# print(len(my))   #9

# # """Метод count"""
# my_str="Молоко"     #3 буквы - о
# print(my_str.count("о"))
# my="Kyrgyzstan"
# print(my.count("y"))

# # False ложь
# # True  истина
# # """Метод . isdigit"""
# a="54"
# b="text"
# print(type(a))   #str
# print(a.isdigit())  #true
# print(b.isdigit())  #false


# # """Метод .isalpha()"""
# print(b.isalpha())
# print(a.isalpha())

# a="apple and banana"
# print(a.startswith("a"))   #true
# print(a.startswith("b"))    #false

# b="banana-and milk"
# print(b.endswith("k"))  #true
# print(b.endswith("l"))  #fasle

# # """Метод. split()"""-разделить строку
# print(type(b.split()))
# print(b.split())
# print(b.split("-"))

# my_text="p*y*t*h*o*n"
       # """срезы-индексы"""
# my_text="python"
# print(my_text[0]) #p
# print(my_text[1]) #y
# print(my_text[2]) #t
# print(my_text[5]) #n
# print(my_text[-1]) #n

# # my_text[6-1]=>my_text[5]
# print(my_text[len(my_text)-1])  #n
# print(my_text[0:2])   #py
# print(my_text[0:3])   #pyt
# print(my_text[0:4])   #pyth
# print(my_text[2:])   #thon
# print(my_text[:])   #python
# print(my_text[:3])   #pyt
# print(my_text[0:6])   #python
# print(my_text[::-1])   #nohtyp
# print(my_text[0:6:2])   #pto
# print(my_text[0:6:3])   #pth
# print(my_text[-4:-1])   #tho

       #    """Условия-if, elif, else"""

# num = int(input("Введите число:"))

# if num > 5:
#     print(f"{num} больше 5")
# elif num == 5:
#     print(f"{num} равно 5")
# elif num == 4:
#     print(f"{num} равно 4")
# else:
#     print(f"{num} меньше 5")    

# a=input("как ваше имя:")
# b=input("скалько вам лет:")
# c=input("ваш любимый фильм:")
# print(f"привет {a}  {b} {c} отлтичный фильм")






# Python = """высокоуровневый язык программирования общего 
# назначения с динамической строгой типизацией и автоматическим управлением 
# памятью, ориентированный на повышение производительности разработчика, 
# читаемости кода и его качества, а также на обеспечение переносимости 
# написанных на нём программ."""

# python="Python Language gg fr"
# print(len(python. replace(" ","")))

# new_python=python.split(" ")
# print(new_python)  # python="Python Language gg fr"
# print(len(new_python))