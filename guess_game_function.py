import random
name = input("Hey, What's your name?  \n")
print("Welcome to this game, ", name ,  ".", "This is a 'Guess number game' , I will think of a number between 0 and 50 and I will give you 5 tries to guess it ;)")

def numbergame():
    game_number = random.randint(0,50)
    i = 1
    r = 1
    while i <6:
        user_number = int(input("What is your guess?  \n"))
        if user_number < game_number:
            print(name , " , my number is bigger.. ")
            i = i+1
        elif user_number > game_number:
            print(name, " , my number is smaller..")
            i = i+1
        elif user_number == game_number:
            print("\n Nice, ", name , "you guessed my number! :) ")
            r = 0;
            break
    if r == 1:
        print("\n Sorry, maybe you'll guess it next time ;) ")
        print("my number was: ", str(game_number))

def main():
    numbergame()
    while True:
        again = input("\n Do you wish to play again? (yes/no):  ")
        if again == 'yes':
            numbergame()
        else:
            break
main()
print("See you soon!")
            
