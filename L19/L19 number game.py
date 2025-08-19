import random

number = str(random.randint(10,20))
print("Guess number between 10  until 20")

while True:
    print("give me your best guess!")
    guess = input()
    print()

    if number == guess:
        print("you win the game!")
        print("the number was ",number)
        break
    else:
        print("your guess isn't quite right, try again.")
        print()