# problem 1
# обьедените словари 

#dic1 = {1:10, 2:20}
#dic2 = {3:30, 4:40}
#dic3 = {5: 50,6: 60}

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
lst=[]
lst.append(dic1)
lst.append(dic2)
lst.append(dic3)
print(lst)

# problem 2
# Ниже представлены два списка . Напишите программу Python для преобразования их в словарь 
# таким образом, чтобы элемент из списка 1 был ключом, а элемент из списка 2 - значением.

#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

python=dict(zip(keys, values))
print(python)
d={}
d[keys[0]]=values[0]
d[keys[1]]=values[1]
d[keys[2]]=values[2]
print(d)




# problem 3
#
# Распечатайте значение ключа 'history', как показано ниже. dict

#sampleDict ={"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}

# Ожидаемый результат:
# 80
sampleDict ={"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
print(sampleDict['class']['student']['marks']['history'])


# problem 4
# Напишите программу Python для создания нового словаря путем извлечения
#  упомянутых ключей из приведенного ниже словаря.

# sample_dict = {"name": "Kelly","age": 25,"salary": 8000,"city": "New york"}

# ключи которые надо вывести
# keys = ["name", "age"]

sample_dict = {"name": "Kelly","age": 25,"salary": 8000,"city": "New york"}
print(sample_dict.keys())
