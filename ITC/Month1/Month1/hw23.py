# class Solution(object):
#     def runningSum(self, nums):
#         res=[]
#         count=0
#         for i in nums:
#             count += i
#             res.append(count)
#         print(res)
# n=Solution()
# n.runningSum([1,1,1,1,1]) 

# Напишите программу, которая считывает список чисел lst из первой 
# строки и число x из второй строки, которая выводит все позиции, на 
# которых встречается число x в переданном списке lst.
# Позиции нумеруются с нуля, если число xx не встречается в списке, 
# вывести строку "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
# Sample Input 1:
# 5 8 2 7 8 8 2 4
# 8
# Sample Output 1:
# 1 4 5
# Sample Input 2:
# 5 8 2 7 8 8 2 4
# 10
# Sample Output 2:
# # Отсутствует
lst= [5, 8, 2, 7, 8, 8, 2, 4]
num = 8
if num in lst:
    for i in range(len(lst)):
        if num == lst[i]:
            print(i)
            break
else:
    print("Отсутствует")
print("")
# print(lst.index(num))    
# # problem2
# # создайте программу которая приветствует на разных языках с помощью def,for,if
# # и импортируйте в другой файл
good=['hi','здравстуйте','саламатсызбы']
def my_prog2():
    for i in good:
        if i ==i:
            print(i)
my_prog2()
print("")
# #Problem3
# # Напишите функция для бота, которая принимает параметр hours и умеет 
# # здороваться утром и днём, но ей нужно добавить приветствия для ночи и вечера. 
# # Напишите условную конструкцию, которая выводит уместные сообщения:
# # ВРЕМЯ ТЕКСТ ПРИВЕТСТВИЯ
# # до 6 Доброй ночи!
# # до 12 Доброе утро!
# # до 18 Добрый день!
# # до 23 Добрый вечер!
# # в остальных случаях Доброй ночи!
# # Подсказка
# # Создайте конструкцию if-elif-else с тремя elif и логическим оператором <.
# # Ключевые слова elif и else должны располагаться точно под if
# # После условий в elif и после ключевого слова else нужны двоеточия.
# # Блоки кода под elif и else должны отбиваться четырьмя пробелами.
hours=int(input("Введите время: "))
if 0 < hours < 7:
    print ("Доброй ночи") 
elif 6 < hours < 12:
    print ("Доброе утро!") 
elif 11 < hours < 17:
    print ("Добрый день!") 
elif 18 < hours < 23:
    print ("Добрый вечер") 
else:
    print('Доброй ночи!')
print("")
# # Problem4
# # Напишите функцию, которая принимает число "n", вам нужно вывести цифры от 1 до "n", 
# # как показано на результате
# # n = 4
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
ls=''
n = 5
for i in range(n):
    for y in range(i):
       ls = (str(i) + ' ')*i 
    print(ls)
print("")        
# # 5. Дан список гостей, на сегодняшную вечеринку :
# # guests = ['Axe', 'Tom', 'Jax', 'Rik', 'Sam', 'Zot']
# # Создай цикл while чтобы проверить приходящих гостей.
# # Если человек вводит имя которое нет в списке то выводи
# # Сообщение: Извините, ваше имя нет списке. Sorry.
# # Если человек вводит имя которое есть в списке то выводи
# # Сообщение: Добро пожаловать гость заходите и наслаждайтесь.
while True:
    guests = ['Axe', 'Tom', 'Jax', 'Rik', 'Sam', 'Zot']
    a=input("Напишите свое имя: ")
    for i in list(guests):
        if i == a:
            print("Добро пожаловать гость заходите и наслаждайтесь")
            break
    else:
        print("Извините, ваше имя нет списке") 
        break
print("")
# 6 Создай программу которая проверяет сложность пароля:
# Если длина пароля:
# меньше 4: <<очень легкий>>.
# больше 4 и меньше 8: <<простой>>.
# больше 8: <<надежный пароль>>.
# Продолжайте спрашивать <<надежный пароль>> пока клиент не введет сложный пароль
# Если клиент вводит очень легкий пароль выводи
# Сообщение: Пвв твой пароль даже школьник взломает
# Если клиент вводит простой пароль выводи
# Сообщение: Я взломаю твой пароль за пару секунд зуб даю
# Если клиент вводит надежный пароль выводи
# Сообщение: Хмм твой пароль довольно сложный, Молодец
password=input("Введите пароль: ")
if len(password)==0:
    print("Напишите еще раз ваш пароль")
elif  len(password) <= 4:
    print("Очень легкий Пвв твой пароль даже школьник взломает")
elif 4 < len(password) <= 8:  
    print("Простой, Я взломаю твой пароль за пару секунд зуб даю")
elif len(password) > 8:
    print("Пароль надежный, Хмм твой пароль довольно сложный, Молодец")    