# 1. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

# n = float(input('n =  '))
# sum = 0
# for i in str(n):
#     if i != '.':
#         sum+=int(i)
# print(sum)

# 2. Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
# n = int (input ('n = '))
# m = 1
# for i in range (1, n+1):
#     m*=i
#     print(m)

# 3.Задайте список из n чисел последовательности (1 + 1/n) ** n 
# и выведите на экран их сумму.
# n = int (input ('n = '))
# sum = 0
# for i in range(1, n+1):
#     sum+=(1 + 1/i) ** i
# print(sum)
 
 
# 4. Перемешивание
# import random
# list = [1, 2, 3, 4, 5]
# result = random.sample(list, len(list))
# print ('\n', str(list), ' --> ', str(result), '\n')