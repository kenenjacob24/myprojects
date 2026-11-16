import random

number = random.randint(1,10)

guess = int(input("Guess a number from 1 to 10 ",))

if guess == number:
    print("you are correct!")

else:
    print("sorry you are wrong!")
    print("The correct number was", number)
