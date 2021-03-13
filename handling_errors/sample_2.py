# input validation

num_cats = input('How many cats do you have? ')
try:
    if int(num_cats) >= 4:
        print('That is a lot of cats.')
    elif int(num_cats) == 0:
        print('You do not have a cat.')
    elif int(num_cats) < 0: 
        print('You entered a negative number.')
    else: 
        print('That is not that many cats')
except ValueError:
    print('You did not enter a number.')