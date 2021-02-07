# This is a guessing game
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I ame thinking of a number between 1 and 20.')

for guessesTaken in range(6):
    print('Take a guess.')
    your_guess = input()
    your_guess = int(your_guess)

    if your_guess < number:
        print('Your guess is too low. ')

    if your_guess > number:
        print('Your guess is too high. ')

    if your_guess == number:
        break
if your_guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if your_guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
