import random
import math

print('Welcome to guess the number!')
print('The rules are simple. I will think of a number and you will guess it')

low = int(input('Enter a lower bound number'))
high = int(input('enter a higher bound number'))

x = random.randint(low, high)
y = math.log(high - low + 1,2)
print(y)
print("\n\tYou have only", round(y), " chances to guess the interger! \n")

count = 0

while count < y:
    count += 1
    guess = int(input('Guess a number:- '))

    if x == guess:
        print( "congradulations! you have done it in", count , "try")
        break
    elif x > guess:
        print('you guessed too small')

    elif x < guess:
        print('you have guess too high')

if count >= y:
    print("\nThe number is %d" % x)
    print('better luck next time!')
