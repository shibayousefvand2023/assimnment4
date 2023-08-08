name = ('hello shiba')

import numbers
import random
print('Enter num between 0, 20')
user_number= int(input('enter your gass number:'))
pc_number=random.randint(1,20)
count=1
while 1 :
    if user_number==pc_number:
        print("great")
        print('great' , count , 'press')
        break
if user_number > pc_number:
    print("try again")
    user_number = int(input('enter your gass number:'))
    count+=1
if user_number < pc_number:
    print("Errore!")
    user_number = int(input('enter your gass number:'))
count+=1

