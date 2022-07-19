# #    """ Dictionary- словарь - хеш таблица, """

dct=dict({"ru":"Pussian","kg":"Kyrgyz"})
print(dct)

dct2={"en":"English",5:"five",True:[545,87, False],"tuple":(54,8532)}
print(dct2)
print(len(dct2))

print(dct2["en"])
print(dct2["tuple"])
print(dct2[True])
print(dct2[5])
print(dct2[True][1]+ dct2[True][0])
dct2[5]="пят"             # изменить значания
print(dct2)
dct2[True][2]=10
print(dct2)

del dct2[5]             #удалить значения
print(dct2)

del dct2["tuple"]
print(dct2)

menu={}
menu["besh_barmak"]=130
menu["lagman"]=120
menu["lagman"]=135
menu["borsh"]=90
print(menu)
del menu["borsh"]
print(menu)


drinks=["Coca-Cola","Fanta","Sprite"]
menu["drinks"]=drinks
print("drinks")



names={}
name=input("input yuor name:")
profession=input("input your profession:")
names["name"]=name
names["profession"]=profession
print(names)

#    """Методы у обьета класса <dict>:keys(),values(),items()"""


dct2={"en":"English",5:"five",True:[545,87, False],"tuple":(54,8532)}
print(dct2.keys())                    #вывести на терминале все ключи у словаря dct2
print(dct2.values())                  #вывести на терминал все значения у словаря dct2
print(dct2.items())                   #вывести на терминале все ключи и значения у словаря dct2