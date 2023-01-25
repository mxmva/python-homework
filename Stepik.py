a = int (input())
b = int (input())
c = int (input())
maxx = max(a,b,c)
second_maxx = min(a,b,c)
lost_num = 0
if (a==maxx and b==second_maxx) or (a==second_maxx and b==maxx):
    lost_num = c
   
elif (b==maxx and c==second_maxx) or (b==second_maxx and c==maxx):
    lost_num = a
   
elif (a==maxx and c==second_maxx) or (a==second_maxx and c==maxx):
    lost_num = b 
  
# if a !=second_maxx:
    # lost_num = a
# elif b !=second_maxx:
#     lost_num = b
# elif c !=second_maxx:
#     lost_num = c
print(maxx)
print(second_maxx)
print(lost_num)