curse="ITCBootcamp"
print(curse[:3])
print(curse[3:])

#ITC

#[a,b,c]
#a-start
#b-end
#c-step
city="newyork"
print(city[:3].title(), city[3:].title())
print(city[:3].title()+" " +city[3:].title())
print("{0} {1}".format(city[:3].title(), city[3:].title()))
print(f"{city[:3].title()} {city[3:].title()}")
print(city[0].upper()+city[3].upper())
print("количества буква n ",city.count("n"))
print("количества буква e ",city.count("e"))
print("количества буква w ",city.count("w"))
print("количества буква y ",city.count("y"))
print("количества буква o ",city.count("o"))
print("количества буква r ",city.count("r"))
print("количества буква k ",city.count("k"))
frukts="banana, banana, apple and banana"
print("количества слова banana ",frukts.count("banana"))
print("количества слова apple ",frukts.count("apple"))


nameSchool=input("Введите называния вашей школы: ")
if nameSchool.isalpha():
    print("Да, верно!")
else:
    print("Вы ввели неверный называния школы")    

age=int(input("Введите ваш возраст"))
if age==20:
    print(" Вам 20 лет")
elif age > 18:
    print(" Вам больше  18 лет")
else:
    print("Вам меньше 18")  

num1=int(input("первое число "))          
num2=int(input("второе число "))
if num2==0:
    print("на 0 делит нельзя")
else:     
    print(num1/num2)

num=int(input("Введите число "))
if num>0:
    print("положительное число ")

else: 
    print("отрицательное число ")

n=int(input("Введите число "))
if n % 2==0:
    print("четное число")
else:
    print("нечетное число")


n1=int(input("Введите число "))
if n1 % 3==0 and n1 % 5==0:
    print("FizzBuzz")
elif n1%3==0:   
    print("Fuzz")
elif n1%5==0:
    print("Buzz")    
else:
    print(n1)

#                Boolean
# True  False

# or +
# and* -

print(5>7) #False
print(7>7) #False
print(8>7 and 5>4)  #True
# t and t=>t
print(5>7 and 5>4)  #False
#     F and   T=> F
print(10>7 and 1>4)  #False
#      T and  F=>F
print(5>6 and 4<3)   #False
#     F  and  F=>F
#   or( или)
print(5>2 or 5>3)     #T T or T>T
print(5>2 or 7>8)     #T T or F>T
print(4>1 or 5>2)     #T T or T>T
print(4!=1 or 5<2)    #T T or F>T 
print(4==1 or 5>2)    #T F or T>T 
print(4==1 or 5<2)    #F F or F>F
# #  != не равно
age=int(input("Жаш: "))
if age>18 or age == 18:
    print("Толтурса болот!")
elif age<18:
    print("Болбойт")
else:
    print("Туура сан кийир") 