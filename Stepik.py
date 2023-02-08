# a = int (input())
# b = int (input())
# c = int (input())
# maxx = max(a,b,c)
# second_maxx = min(a,b,c)
# lost_num = 0
# if (a==maxx and b==second_maxx) or (a==second_maxx and b==maxx):
#     lost_num = c
   
# elif (b==maxx and c==second_maxx) or (b==second_maxx and c==maxx):
#     lost_num = a
   
# elif (a==maxx and c==second_maxx) or (a==second_maxx and c==maxx):
#     lost_num = b 
  
# # if a !=second_maxx:
#     # lost_num = a
# # elif b !=second_maxx:
# #     lost_num = b
# # elif c !=second_maxx:
# #     lost_num = c
# print(maxx)
# print(second_maxx)
# print(lost_num)


# Подсчет программистов

# n = int(input())
# if (n % 10 == 1) and (n%100!=11):
#     print(n,'программист')
# elif(n % 10 == 2 and n%100!=12) or (n % 10 == 3 and n%100!=13) or (n % 10 == 4 and n%100!=14):
#     print(n,'программиста')
# elif(n%10==0)or((n%10 ==5)or(n%10 ==6)or(n%10 ==7)or(n%10 ==8)or(n%10 ==9))or((n%100 ==11)or(n%100 ==12)or(n%100 ==13)or(n%100==14)):
#     print(n,'программистов')

# ВАРИАНТЫ РЕШЕНИЯ
# № 1
# a=int(input())
# if 2<=a%10<=4 and not 12<=a%100<=14:
#   b='программиста' 
# elif a%10 ==1 and a%100!=11:
#   b='программист'
# else:
#   b='программистов'

# print(str(a), b)

# № 2
# n, s = int(input()), "программист"

# if 10 < n % 100 < 15: s += 'ов' 
# elif  1 < n % 10 < 5: s += 'а' 
# elif     n % 10 != 1: s += 'ов' 

# print(f'{n} {s}')

# num = input()#123123
# n = int(num)%10
# n1=(int(num)//10)%10 #3
# n2=(int(num)//100)%10
# n3=(int(num)//1000)%10
# n4=(int(num)//10000)%10
# n5=(int(num)//100000)%10
# sum_1=n+n1+n2
# sum_2=n3+n4+n5
# if sum_1==sum_2:print('Счастливый')
# else: print('Обычный')
# print(n,n1,n2,n3,n4,n5)

# a=int(input())
# sum=a
# while a!=0:
#     a=int(input())
#     sum+=a
# print(sum)

# a=int(input())
# b=int(input())
# d=1
# while d%a!=0 or d%b!=0:
#     d+=1
# print(d)
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)

# a=0
# while a<=100:
#     a=int(input())
#     if a>100:
#         break
#     if a<10:
#         continue
#     print(a)

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())

# for g in range (c,d+1):
#     print('\t'+str(g),end='')
# print(end='\n')
# for i in range (a,b+1):
#     print(str(i)+'\t',end='')
#     for j in range (c,d+1):
#         print(str(i*j),end='\t')
#     print(end='\n')
# Альтенативное решение
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())

# print('\t', *range(c, d+1), sep='\t')
# for i in range(a,b+1):
#     print(i, *range(i*c,(i*d)+1, i), sep='\t')

# a=int(input())
# b=int(input())
# summ=0
# count=0
# for i in range(a,b + 1):
#     if i % 3 == 0:
#         summ=summ+i
#         count+=1
# print(float(summ/count))

# strg = input()
# a=strg.upper().count('g'.upper())
# b=strg.upper.count('s'.upper())
# result=(a+b/len(strg))*100
# print((result/len(strg))*100)



# Кодирование осуществляется следующим образом:s = 'aaaabbсaa' преобразуется 
# в 'a4b2с1a2', то есть группы одинаковых символов исходной строки 
# заменяются на этот символ и количество его повторений в этой позиции строки.
# Напишите программу, которая считывает строку,
#  кодирует её предложенным алгоритмом и выводит закодированную 
# последовательность на стандартный вывод. 
# Кодирование должно учитывать регистр символов.

# strr='aaaabbcaa'
# newstr=''
# count=1
# for i in range(len(strr)):
#     if i+1 < len(strr) and strr[i]==strr[i+1]:
#         count+=1
#     else:
#         newstr=newstr+strr[i]+str(count)
#         count=1
# print(newstr)

# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)

# strr=[int(i)for i in input().split()]
# summ=0
# i=0
# while i < len(strr):
#     summ+=strr[i]
#     i+=1
# print(summ)
# Альтернативное решение
# print(sum(int(i) for i in input().split()))