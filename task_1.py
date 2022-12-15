weekDay = [1,2,3,4,5,6,7]
day = int (input('Введите номер для недели'))
if day == weekDay[0] or weekDay[1] or weekDay[2] or weekDay[3] or weekDay[4]:
    print ('Ты все еще работаешь') 
elif weekDay[5] or weekDay[6]:
    print  ('Ура, выходной') 
else:
    print ('Вы вввели несуществующйи день недели')