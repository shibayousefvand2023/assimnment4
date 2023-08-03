import numbers
import random


pc_number=random.radiant(1,20)
count=1
for i in range (20):
    user_number=int(input("Enter number between 0, 20 :"))
    if user_number==pc_number:
        print("great")
        print('great' , count , 'press')
        break
if user_number < pc_number:
    print("try again")
if user_number > pc_number:
    print("Errore!")
count+=1


