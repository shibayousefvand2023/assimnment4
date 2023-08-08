import random


name =('wellcome shiba')

n=int(input('Enter your Non-repeating random numbers:'))
def Non_repeating_random_numbers (n):
    initial_list= list(range(1 , n+15))
    random.shuffle(initial_list)
    my_list= initial_list[:n]
    return my_list
    result = Non_repeating_random_numbers (n)
    print('my_list:' , result)
