# Problem 1
# Выведи на экран, которые существуют как в наборе fruits1, так и в наборе fruits2:
# fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
# fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
print(fruits1.difference(fruits2))
print(fruits2.difference(fruits1))

# Problem 2
# Выведи на экран, являющееся пересечением множеств fruits1 и fruits2:
# fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
# fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
fruits1= { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
fruits1.intersection_update(fruits2)
print(fruits1)

# Problem 3
# Выведи на эркан элементы, входящие в fruits1 или в fruits2, но не в оба из них одновременно:
#fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
#fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
print(fruits1.symmetric_difference(fruits2))

# Problem 4
# Обьедини два множества fruits1 и fruits2:
#fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
#fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
fruits1.update(fruits2)
print(fruits1)

# Problem 5
#predmets = {'биография','математика','химия','биология','физика','астрономия'
#,'123Физ','Гастрономия','Книги','Литература'}
# Удали из списка предметов ненужные предметы Например: 123Физ, Гастрономия
predmets = {'биография','математика','химия','биология','физика','астрономия'
,'123Физ','Гастрономия','Книги','Литература'}
predmets.discard('123Физ')
predmets.discard('Гастрономия')
predmets.discard('биография')
predmets.discard('Книги')
print(predmets)
