"""Guess number game"""
import random
attempt = 0

print("""
I have a number in mind between 1 and 10.

Do you want to guess it?

You have 3 tries!

Enjoy :)
""")
letsstart = input("Do you want to start? (yes/no):  ")

if letsstart == 'yes':
    print("Let's start")
else:
    print("Ok, see you :) ")

    
computernumber = random.randrange(10)
print("I think of a number between 0 and 10")

while attempt < 3:
    guess = int(input("What is your guess?:  "))

    attempt = attempt + 1

    if guess == computernumber:
        break
    
    elif guess <= computernumber:
        print("My number is bigger than yours")

    elif guess >= computernumber:
        print("My number is smaller than yours")

    

if guess == computernumber:
    print("Nice, you got it! :-)")
if guess != computernumber:
    print("try it again ;-) ")

    

    

    
