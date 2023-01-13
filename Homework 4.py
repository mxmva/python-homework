#Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N. 
# number = int(input('Enter number ' ))

# N = int(input('Задайте натуральное число: N = '))
# factors = []
# d = 2
# m = N 
# while d * d <= N:
#   if N % d == 0:
#   factors.append(d)
#   N //= d
# else:
#   d += 1
# factors.append(N) 
# print('{} -> {}' .format(m, factors)) 

# 2. Вычислить число c заданной точностью d
# Пример:- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

pi = 3.141592653589793
d = int(input('Задайте точность вычисления числа Пи'))
S1 = 3.0
z = 1 
i = 2

while abs(pi - S1) > 0.1**d:
    S1 =S1+4*z/(i*(i+1)*(i+2))
    i = i+2
    z = -z
print(round(S1, d))