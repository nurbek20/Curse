# Напишите функцию Python, чтобы найти максимальное из трех чисел
a=int(input("Введите число: ")) 
b=int(input("Введите число: ")) 
c=int(input("Введите число: "))
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
print(mx)

# Напишите функцию Python для суммирования всех чисел в списке
lst1=[34,65,54]
summ=0
for i in lst1:
    summ=summ+i
print(summ)

# Напишите программу Python для переворота строки
# --------
# Пример строки: 123qweasd
# Ожидаемый результат: dsaewq321
ls=("123qweasd")
print(ls[::-1])
lst=[]
for i in range(1,len(ls)+1):
    lst.append(ls[-i])
print(lst)
def reverse_text(txt):
    return txt[::-1]
print(reverse_text("123qwesd"))    

# Напишите функцию Python, которая принимает список и возвращает 
# новый список с уникальными элементами первого списка
lst2=[1,1,3,3,6,9,9,7,10,98,10]
def uniq(lst2):
    uniq_elem=set(lst2)
    print(list(uniq_elem))
uniq(lst2)
l=[5,6,5,7,7]

def uniq(l):
    uniq_elem=set(l)
    print(list(uniq_elem))
uniq(l)

# Напишите функцию Python для умножения всех чисел в списке
lst3=[3,8,9,5,7]
summ=1
for i in lst3:
    summ=summ*i
print(summ)
