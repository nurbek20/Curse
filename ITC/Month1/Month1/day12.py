students={"Nurbek","Ulukman","Kumushai","Rustam","Abdulatif","Gulzina"}

name=input("input student's name:")
if name in students:
    print("студент",name)
else:
    print("такого студента нет")    

my_dict={}
my_dict["swim"]="плавать"
print(my_dict)
my_dict["teacher"]="учитель"
my_dict["book"]="книга"
my_dict["run"]="бегать"
my_dict["mouse"]="крыса"
my_dict["laptop"]="ноутбук"
print(my_dict)

english_word=input("Введите слова на английском для перевода на русский:")
print(english_word,"-",my_dict[english_word])
if english_word in my_dict:
    print(my_dict[english_word])
else:
    print("нет такого словарь")    

"""For, while-цикл"""
numbers=[12,45,78,52,47,502,47, 547]
print(numbers[0])  #12
print(numbers[1])  #45
print(numbers[2])  #78
print(numbers[3])  #52
print(numbers[4])  #47

for i in numbers:  #
    print(i)


print(range(11))       #0,1,2,3,4 ... 11
print(range(5, 11))      #5,6,7 ... 11
print(range(5, 11, 2))    # 5,7, ...

for i in range(len(numbers)):     # range => 0,1,2,3,4,5
    print(numbers[i])          # 1) i=0              2)i=1                    3)i=2
#                           #print(numbers[0])=12  print(numbers[1])=45   print(numbers[2])=78
# 4)i=3                    5)i=4                      6)i=5
#print(numbers[3])=52     print(numbers[4])=47    print(numbers[5])=502

for i in numbers:  #1) i=12        2)i=45
    print(i)        # print(12)    print(45)

my_list=[54,45,1,2,8,12]
for i in range(len(my_list)):
    if  my_list[i]>5:
        print(my_list[i])

my_list2=[15,485,-8,85,-15,-478,231]
for i in range(len(my_list2)):
    if my_list2[i]<0:
        print(my_list2[i])        
for i in my_list2:
    if i>0:
        print(i)

for i in range(len(my_list2)):
    if my_list2[i] % 5 ==0:
        print(my_list2[i])

for i in range(1,6):
    print(i)

for i in range(0,7,3):
    print(i)

for i in range(10,61,2):
    print(i)

for i in range(11,61,2):
    print(i)

my_list2=[15,485,-8,85,-15,-478,231]
for i in range(len(my_list2)):
    print("индексы",i,my_list2[i])