# 1)
# Напишите функцию для печати четных чисел из заданного списка

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# пример вывода:
#  [2, 4, 6, 8]
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def num(lst):
    ls = []
    for i in lst:
        if i % 2 == 0:
            ls.append(i)
    print(ls)
num(lst)            


# 2)Напишите функцию которая принимает список и возвращает новый список
#  с уникальными элементами первого списка.
# [1,2,3,3,3,4,4,4,4,5,6,6,7,8,8,8]
# Пример вывода:
#   [1, 2, 3, 4, 5]
num1=[1,2,3,3,3,4,4,4,4,5,6,6,7,8,8,8]
def unique_numbers(num1):
    unique = []
    for i in num1:
        if i in unique:
           continue
        else:
            unique.append(i)
    return unique
print(unique_numbers(num1))
unique_numbers(num1)

def uniq(num1):
    uniq_elem=set(num1)
    print(list(uniq_elem))
uniq(num1)

def uniq(num1):
    uniq_elems=set(num1)
    return list(uniq_elems)
print(uniq(num1))    

# 3)Найдите самый большой элемент из данного списка
#   Используйте встроенную функцию max (), чтобы получить наибольшее число из списка
# x = [4, 7, 8, 24, 12, 2, 1]

x = [4, 7, 8, 24, 12, 2, 1,58]
max_num = 0
for i in x:
    if i > max_num:
        max_num = i
print(max_num)

def num2(x):
    max_num=0
    for i in x:
        if i>max_num:
            max_num = i
    print(max_num)
num2(x)                

def find_max(x):
    return max(x)
print(find_max(x)) 

def find_max2(x):
    max_num=x[0]
    for i in x:
        if max_num<i:
            max_num=i
    print(max_num)
find_max2(x)        