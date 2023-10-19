import random
number = random.randint(1,10)
guess_number = 10
while guess_number != number:
    guess_number =int(input("Enter the guess number:"))
    if guess_number < number:
        print("Guess higher!!")
    elif guess_number> number:
        print("Guess lower!!")
    else:
        print("COngratulations!!You WON!!")
        