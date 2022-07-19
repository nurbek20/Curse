#1).Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, 
# и возвращающую True, если оно простое, и False - иначе.
#Простые числа, это такие числа, которые не имеют никаких других делителей,
#  кроме едицы и самого себя. 7, 41, 53 — простые числа. Составные числа, это 
# такие числа, которые имеют другие делители, кроме едицы и самого себя. Число 
# 1 выделяют особо — оно не относится ни к простым ни к составным число
def is_prime(n):
    if n < 2:
       return False
    if n == 2:
       return True
    num = n**(1/2)
    i = 2
    while i <= num:
       if n % i == 0:
           return False
       i += 1
    return True
print(is_prime(int(input("Введите число: "))))

def is_prime(num):
    if num  != 0 and num % 2 == 0 and num % num == 0:
        print(True)
    else:    
       print(False)
is_prime(7)
is_prime(41)
is_prime(53)
is_prime(54)
    
#2).Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
#  и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
season=int(input("Введите номер месяца: "))
if 0 < season < 4:
    print ("Зима") 
elif 3 < season < 7:
    print ("Весна") 
elif 6 < season < 9:
    print ("Лето") 
elif 8 < season < 12:
    print ("Осень") 
else:
    print('неверная команда')
   
#3) найти средние арифметическое
# человек водит числа, потом надо вывести средние арифметическое этих чисел
# решить только через функцию 

a = int(input('a число: '))
b = int(input('b число: '))
c = int(input('c число: '))
l = [a,b,c]
def number_l(l):
    summ=0
    count=0
    for i in l:
        summ=summ+i
        count=count+1
    print(summ/count)
number_l(l)


#4)создать функцию которая принимает арогумент виде текста и выводить 
# текст без пробелов
text=("создать функцию которая принимает арогумент виде текста")
def my_text(text):
    print(text.replace(" ",""))
my_text(text)  
# 5)Человек вводит пять чисел по отдельности, вы должны их всех поместить в
#  список и все четные числа вывести в консоль.
a1=int(input("Введите число: "))
a2=int(input("Введите число: "))
a3=int(input("Введите число: "))
a4=int(input("Введите число: "))
a5=int(input("Введите число: "))
lst=[]
lst.append(a1)
lst.append(a2)
lst.append(a3)
lst.append(a4)
lst.append(a5)
print(lst)
for i in lst:
    if i % 2==0:
        print(i)
        
# 6)Вы дожлны записать имя, возраст, пол троих студентов Backend 
# группы и вывести 
# их по отдельности в цикле.
dict={}
dict["Nurbek"]=26
dict["Ruslan"]=13
dict["Ulukman"]=16
print(dict)
for i in dict:
    print(i,dict[i])

group={}
for i in range(3):
    name= input("Name: ")
    group[f"Имя{i}"]= name
    age=int(input("Age: "))
    group[f"Возраст{i}"]= age
    gender=input("Gender: ")
    group[f"Пол{i}"]=gender

print(group)    

