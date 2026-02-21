import random
num = random.randint(1,10)
guess=int(input("guess the number between 1 and 10 : "))

while guess!= num:
    if guess<num:
        print("your guess is too low")
    elif guess>num:
        print("your guess is too high")
    
    guess=int(input("guess again: "))
print("you guessed it right")