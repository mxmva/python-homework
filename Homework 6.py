# 1.Создайте список из случайных чисел. 
# Найдите количество различных элементов в нем.

# import random
# list = [random.randint(1,9) for _ in range(10)]
# print(list)
# list.sort()
# print(list)
# count = 1
# for i in range(len(list)-1):
#     if list[i]!=list[i+1]:
#         count+=1
# print(count)



# 2. "Пора учить английский язык", - сказал себе Степа и решил написать программу 
# для изучения английского языка. 
# Программа получает на вход слово на английском языке и несколько его 
# переводов на русском языке. Составьте словарь, в котором ключ - это английское слово,
#  а значение - это список русских слов. 
word = 'oringe - апельсин, оранжевый, рыжий'.split(' - ')
dict = {word[0]: word[1].split(', ')}
print(dict)
