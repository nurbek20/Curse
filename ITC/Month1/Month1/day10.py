lst2=[True,"Text",54,45.5,["New",97,54]]
print(lst2[4][1]+lst2[4][2])
print(lst2[4][0])
print(lst2[1].startswith("1"))
a="Text"
if a.startswith("T"):
    print(True)
else:
    print(False)
my_list=[8, 8, 8, 4, 5, 8]
my_list.insert(0, True)
my_list.insert(5, False)
print(my_list)
my_list.pop(4)
del my_list[0]
del my_list[-1]
print(my_list)

students=[]
name1=input("Введите ваше имя студента: ")
name2=input("Введите ваше имя студента: ")
name3=input("Введите ваше имя студента: ")
name4=input("Введите ваше имя студента: ")
name5=input("Введите ваше имя студента: ")
students.append(name1)
students.append(name2)
students.append(name3)
students.append(name4)
students.append(name5)
print(students)


dct={"name":"Alina","age": 15, "gender":"woomen","is_student":False,
"colors":["blak","white","yellow"]}
print(dct)
print(type(dct))             #dct
print(len(dct))
print(dct["name"])
print(dct["name"],"is favorite color",dct["colors"][2])

dct["is_pupil"]=True        # Дабавить новый ключ и его значения
print(dct)

dct["age"]=20               #  Изменить значения существующего  ключа
print(dct)
del dct["is_student"]
print(dct)
fd={458:"True", 45:78}
sd={"turn":"True", "text":78}
fd.update(sd)
print(dct)                   #{458: 'True', 45: 78, 'turn': 'True', 'text': 78}
print({**fd, **sd})          #458: 'True', 45: 78, 'turn': 'True', 'text': 78}


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

sampleDict ={"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
print(sampleDict['class']['student']['marks']['history'])
print(sampleDict['class']['student']['name'])
print(len(sampleDict))
del sampleDict["class"]["student"]["marks"]["physics"]
print(sampleDict)