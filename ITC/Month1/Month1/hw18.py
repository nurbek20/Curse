#1
# с помощью list comprehenstion операций вывести в списке нечетные числа
# lts = [1,2,3,4,5]
# lst = [1,2,3,4,5]
# lst1=[items for items in lst if items%2!=0]
# print(lst1)

#2
# с помощью тернарного оператора вывести сумму,произведения,разность
lts = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
lst2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
summ=0
count=1
for i in lst2:
    summ += i
    count *= i
print(summ)    
print(count)

#3
# сделать калькулятор с выбором операция если пользователь ввел 
# знак, который не является знаком арифметической операции то вывести
#  сообщение о некорректном вводе необходимо проверить не является ли 
# нулем второе число. Если это так, то сообщить о невозможности деления
while True:
    s=input("Введите знак(/,*,-,+): ")
    if s =='0':
        break
    if s not in ('/','*','-','+'):
        quit()
    a=float(input('Введите число: '))
    b=float(input('Введите число: '))
    if s=='+':
        print(a+b)
    elif s == '-':
        print(a-b)
    elif s == '*':
        print(a*b)
    elif s == '/':   
        if b  != 0:
            print('на ноль делить нельзя')   
        else:
            print("на ноль делит нельзя")    