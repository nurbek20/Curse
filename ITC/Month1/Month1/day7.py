#       """List-Список-Массив"""
a = 56      # int
c = 55.2    #float 
b = "Text"  #str
# 1 способ
#   0     1      2        3   4
lst=[53, True, "python", 54.3,545]
#  -5    -4     -3       -2  -1
print(type(lst))   # list

# 2 способ
lst2=list([54,565, True, False])
print(type(lst2))
print(lst2)
print(len(lst2))
print(lst[0])
print(lst[-1])
print(lst[2])
print(lst[-3])

    # lst.append("Web site")
name="Aida"
lst.append(name)
lst.append(545)
lst.append(True)
lst.append("True")
print(lst)
lst.append([True,"good","email"])
print(lst)
print(len(lst))
#2 способ
lst2=list([54,565,True,False])
# содания пустого списка
empty_lst=[]
empty_lst2=list()
#empty_lst=[]
print(empty_lst)
print(empty_lst2)


animals=[]
animals.append("slon")
animals.append("loshad")
animals.append("karova")
animals.append("sabaka")
animals.append("cat")
print("",animals[-1])
print("",len(animals))


numbers=[55,89,6,55,8,6,44,3,5,7,3]
print(numbers[-2])
print(len(numbers))
print(numbers.count(55))
print(numbers.count(89))
print(numbers.count(6))
print(numbers.count(8))
print(numbers.count(44))
print(numbers.count(3))
print(numbers.count(5))
print(numbers.count(7))

print(numbers.index(6))
print(numbers.index(7)) #для нахожденгия индекса
numbers.remove(55)    # удалить элемент из списка
print(numbers)

numbers.pop()        # по умолчанию удалят последний элекмент
numbers.pop(1)     #удалить элемент по индексу
print(numbers)

numbers.insert(0,5)
numbers.insert(2,100)      # вставляет во второй индекс число 100
print(numbers)

a=[1,2,3,4]
b=[5,6,7,8]
# a.append(b)
a.extend(b)
print(a)
a.clear()    #очистить список
print(a) 
my_list=[545,54,5,45]
new_list=my_list.copy()   #скопирует все списка 
print(new_list)

my_list.sort()      #сортирует список по возростанию
print(my_list)
print(my_list[::-1])

yaer=288
if yaer%100!=0:
    if yaer%4!=0:
        print(yaer)
