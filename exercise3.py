import random

number=random.randint(1,50)
guess = int(input("Please enter number between 1 and 50"))
while guess != number:
    if guess < number:
        guess = int(input("Please increase your number"))
    else:
        guess = int(input("Please decrease your number"))
else:
    print("Congrats you won")
