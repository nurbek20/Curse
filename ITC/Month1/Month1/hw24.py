# 1). Создать функцию, при вызове которой, пользователь вводит число,  и получает 3 
# результата, Сумму этого числа и 18, Куб этого числа (**3) и факториал этого числа.
import math
def my_func(num):
    print(num+18)
    print(num ** 3)
    print(math.pow(num,3))
    print(math.factorial(int(num)))
num2 = float(input("Input number: "))
my_func(num2)    
print("")
# 2). Создать текстовый файл, в котором хранится информация о вашем ноутбуке. 
# И в другом, .ру файле, посчитать количество всех символов в этом текстовом файле.
new_file = open("notebook.txt","w")
new_file.write("model-Acer, \nRAM - 4, \nVideokarta - Intel UHD Graphics, \nprocessor - Core i3")
new_file.close()
my_file2 = open("notebook.txt","r")
# print(my_file2.read())
my_notebook = my_file2.read()
print(len(my_notebook))
# 3). Создать список в day24.py, в котором хранится 5 языков программирования. 
# Вам надо посчитать все СИМВОЛЫ (не объекты) этого листа, и вывести факториал этого 
# числа без модуля Math, и выполнить его в другом файле, не day24.py
import math
from day27 import lang_list
print(lang_list)
print(len(lang_list))
count_letter = 0
for  i in lang_list:
    count_letter = count_letter + len(i)
print(count_letter)
print(f'{count_letter} в факториале {math.factorial(count_letter)}')

n=int(input())
m=(input().split(" "))
m2=[]
for i in m:
    m2.append(int(i))
max1=max(m2)
min1=min(m2)
m3=[]
for i in range(min1,max1+2,2):
    if i>max1:
        break
    else:
        m3.append(i)


h=[]
for i in m2:
    if i!=min1:
        h.append(i)
    min1+=2
set1 = set(m3)
set2 = set(m2)
list3 = list( set1.difference(set2) )




if not list3:
    print(*h)
elif not h:
    print(*list3)