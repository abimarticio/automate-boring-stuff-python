# This is a guess number game.
# User can only guess six times.
import random 


name = input('What is your name? ')
print(f'Well, {name}, I am thinking of a number between 1 to 20. Take a guess.')

secret_num = random.randint(1, 20)
for guessTaken in range(1, 7):
    guess = int(input('Enter a number: '))
    if guess == secret_num:
        print(f'Good job, {name}! You guessed my number in {guessTaken} guesses!')
        break
    elif guess < secret_num:
        print('Your guess is too low.')
    elif guess > secret_num:
        print('Your guess is too high.')

print(f'Nope. The number I was thinking of was {secret_num}.')     