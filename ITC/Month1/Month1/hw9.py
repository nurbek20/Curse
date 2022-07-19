# 1. Дан список(Lists): 
# numbers = [67, 99, 56, 43, 66, 12]
# Посчитать сумму чисел из списка numbers
numbers = [67, 99, 56, 43, 66, 12]
print("сумма всех число",numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]+numbers[5])

# 2. Дан список(Lists): 
# numbersOff = [548, -23, 34, -77, 0, 12, -5, 36, -34, -60, 3, -9]
# Посчитать сумму только отрицательных чисел из списка numbersOff
numbersOff = [548, -23, 34, -77, 0, 12, -5, 36, -34, -60, 3, -9]
print("сумма отрицательных число",numbersOff[1]+numbersOff[3]+numbersOff[6]
+numbersOff[8]+numbersOff[9]+numbersOff[11])

# 3. Записать в список(Lists) все числа в диапазоне от 10 до 2500
Lists=[10,11,13,14,15, ...,2500]
Lists=[10,2500]
Lists=[10,2500]
print(Lists)

#Problem4:
# Удалить из листа [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 
# # все чётные индексы до 10
numbers1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 
numbers1.pop(1)
numbers1.pop(2)
numbers1.pop(3)
numbers1.pop(4)
numbers1.pop(5)
print(numbers1)

# Задача 5
# Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}.
# Объедините их в один при помощи встроенных функций языка Python.
dict_1 = {"a": 300, "b": 400}  
dict_2 = {"c": 500, "d": 600}
dict_1.update(dict_2)
print(dict_1)

# Задача 6
#Создайте словарь, в котором ключами будут числа от 1 до 10,
#а значениями эти же числа, возведенные в куб.
numbers2={}
numbers2[1]=1**3
numbers2[2]=2**3
numbers2[3]=3**3
numbers2[4]=4**3
numbers2[5]=5**3
numbers2[6]=6**3
numbers2[7]=7**3
numbers2[8]=8**3
numbers2[9]=9**3
numbers2[10]=10**3
print(numbers2)