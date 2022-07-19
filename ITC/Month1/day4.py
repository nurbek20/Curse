#? course="Bootcamp"
#? print(course[:3])
#? print(course[3:])

#? city="newyork"
#? # New York
#? print(city[:3].title(), city[3:].title())
#? print(city[:3].title()+" "+city[3:].title())
#? print("{0} {1}".format(city[:3].title(), city[3:].title()))
#? print(f"{city[:3].title()} {city[3:].title()}")
#? print(city[0].upper())
#? print("Кол-во буква 'n': ", city.count("n"))

#? fruits="banana,banana, apple and banana"
#? print("Кол-во буква, 'banana'", fruits.count("banana"))
#? print('Кол-во буква, "apple"', fruits.count("apple"))

# numberOfShchool=input("Введите номер вашей школы: ")
# if numberOfShchool.isdigit():
#     print("Да верно!")
# else:
#     print("Вы ввели неверный номер школы")


age=int(input("Введите ваш возрасть: "))
if age == 20:
    print("Вам 20 лет")
elif age > 18:
    print("Вам болше 18")
elif age < 18:
    print("Вам меньше 18")