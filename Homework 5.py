# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# text ='aбвгдейка, aбвгдейка - это учеба и игра. aбвгэдейка, абвгэбейка, азбуку детям знать пора!'
# new_text = list(filter(lambda x: 'а' not in x and 'б'not in x and 'в' not in x, text.split()))
# print(new_text)

# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
s = 'AAADDDGGGGGEE'
print(s)
count = 1
for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                print(count,s[i])
                count=1
print(count,s[i])

