#      1   2   3    4      5          6
lst = [15, 98, 8, True, "Good", [8, "map", False]]
#       0   1   2   3      4           5
#                                0     1      2
print(len(lst))   # 6
print(lst[5][1])  # map
print(lst[5][2])

lst2 = ["Take", "dog", "eggs"]
# lst.append(lst2)
lst.extend(lst2)
print(lst)
lst3 = [54, 87, 54, 85, *lst2]   
print(lst3)      # [54, 87, 54, 85, 'Take', 'dog', 'eggs']
lst4 = ["Take", "dog", "eggs"]
lst5 = [54, 87, 54, 85]   
lst4.insert(1, "cat")
lst4.remove("Take")

lst4.pop()
del lst4[0]    # удалить значение из списка по индексу
print(lst4)
# print(lst4+lst5)     #  ['Take', 'dog', 'eggs', 54, 87, 54, 85]



numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # Ваша задача вывести на экран:
# #  - количество чисел в списке. 
# #  - получить диапазон от 5 до 15                             [5, 6,7, 8, ... 15] 
# #  - получить обратный (перевернутый) диапазон от 10 до 20.   [20, 19,18, ...  10]

print(numbers[:8:-1])


firt_list = [45, 78, 87, True]
firt_list[3] = "Python"
firt_list[0] = "language"
print(firt_list)   # ['language', 78, 87, 'Python']
first_element = firt_list[0]   # lan  
third_element = firt_list[3]   # Python
second_element = firt_list[1]  # 78
firt_list[0] = third_element
firt_list[1] = first_element
firt_list[3] = second_element
print(firt_list) # ['Python', 'language', 87, 78]


# """Tuple - кортеж  (нельзя добавить новые значения и также удалить значения)"""  

tpl = tuple()  # создать пустой кортеж
tpl2 = ()      # 2й способ создать пустой кортеж

print(type(tpl))  # тип данных  "tuple"
print(type(tpl2)) # тип данных  "tuple"

tpl3 = (True, 454, "python", "book")
tpl4 = tuple((54, "plus", 587, False)) 
print(len(tpl3))   # 4
print(tpl3)
print(tpl4)
print(tpl3[0])   # True
print(tpl3[-1])  # book

 #     0     1     2    3           4
t = ("FGG", 524, True, 54.5, [54,87, 74,87])

a = (1,2,3, 4, 5)
a2 = (6,7,8, 9, 10)
a3 = (10,11,12,13 ,14)
lst = []
# [(1,2,3, 4, 5), (6,7,8, 9, 10),  (10,11,12,13 , 14)]

lst.append(a)
lst.append(a2)
lst.append(a3)
print(lst)