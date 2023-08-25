name = ('hello shiba')
print(name)

import random
print("Enter num between 0-20")
user_number= int(input('enter your gass number:'))
pc_number=random.randint(0,20)
count=1
while 1 :
    if user_number==pc_number:
        print(f"equal {user_number} and {count}")
        break
    if user_number>pc_number:
        print(f"its higher than{user_number}")
        user_number=int(input('enter your gass number:'))
        count+=1
    if user_number<pc_number:
        print(f"its smaller than{user_number}")
        user_number=int(input('enter your gass number:'))
        count+=1

