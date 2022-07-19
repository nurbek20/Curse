#    """Set"""
# множества неупорядочены и поэтому не можем получить по индексу
#  не можем удалить элемент
# множества- контейнер уникальных и неповтаряющихся элементов

my_set=set()
print(my_set)
print(type(my_set))      # set

my_set2=set({45,8,5,9,2})
print(my_set2)
print(type(my_set2))   #set

my_set3={5,8,7,True,"phyton",5.5,7}
print(my_set3)
print(len(my_set3))       #6

my_set4={}
print(type(my_set4))  #dict
print(my_set)
my_set.add("Ulukman")   # добовить новое значения
my_set.add("Nurbek")
my_set.add("Kumushai")
my_set.add("Rustam")
my_set.add("Gulzina")
print(my_set)

my_set4[1]="Nurbek"
my_set4[2]="Ulukman"
my_set4[3]="Kumushai"
my_set4[4]="Rustam"
my_set4[5]="Gulzina"
print(my_set4)

uniq={5,89,74,54,12}
uniq.remove(5)  # удалить значения из множества
#uniq.remove(111)   # выдаст ошибка
uniq.discard(111)     #не получим ошибки
uniq.discard(54)     #удалить значения из множества, если не существует 
# значениято останет без изменения
print(uniq)
uniq.pop()   # удалить первое значения из множества
uniq.pop()
print(uniq)
uniq.clear()    # очистить все элементы
print(uniq)   #set()

f={4,5,6,7}
s={"text","lang","python"}
f.update(s)      #  обьединения двух  set
print(f)

lst=[45,45,87,5]
print(set(lst))   #{5,45,87}
txt="python"
print(set(txt))   #{'o', 'n', 'p', 'y', 'h', 't'}

# st=set()
# a={"3,2,45,5"}
# b={"44,5,34,3"}
# c={"76,8,3,6"}
# st.add(a)
# st.add(b)
# st.add(c)
# print(st)




fset={1,2,3,4}
sset={3,4,5,6}
print(sset.intersection(fset)) # пересечения [3,4]
print(fset & sset)         #пересечения     #{3,4}
fset.update(sset)               #обьдинения {1,2,3,4,5,6}
print(fset)                   
print(fset|sset)                 #обьединения {1,2,3,4, 5, 6}
print(fset.difference(fset))     #разница  {1,2}
print(sset-fset)                 #разница  {1,2}
print(fset.difference(fset))     #разница  {5,6}
print(fset-sset)                 #{5,6}


fset.difference_update(sset)    # пересечения  {3,4}
print(fset)
print(fset.symmetric_difference(sset))    #{1,2,3,4,5,6}
print(fset^sset)                         #{1,2,3,4,5,6}
print(10 in fset)                        #False
print(3 in sset)                         #True



st={34,"python",4,3,5}
st.add(234)
st.pop()
print(st)

methods_of_st={"add","update","remove","uniq","discard","pop","clear",
"difference","symmetric_difference","edifference_updat"}
method_of_dictionary={"update","del","keys","values","pop","clear",
"remove","copy","items"}
print(methods_of_st.intersection(method_of_dictionary))

animals={"slon","phiton","sabaka"}
animals2={"cat","karova","kaban"}
print(animals2.difference(animals))

states={"Kolumbia","Surinam","Brazilia","Urugvai","Chili","Surinam","Paragvai","Panama"}
print(states)
print(list(states))