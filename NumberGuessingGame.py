import random
EASY_LEVEL_ATTEMT=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_choosen):
    if level_choosen=='easy':
        return EASY_LEVEL_ATTEMT=10
    else:
        return HARD_LEVEL_ATTEMPTS=5
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        return attempts-1
    else:
        print(f"your answer is right... The answer was{answer}")


print("enter the number between the range of 1 to 50")
answer=random.randint(1,50)
print(answer)
level =input("choose the level of difficulty.... Type 'easy' or 'hard':")
attempts=set_difficulty(level)
while guessed_number!=answer:
    print(f"you have {attempts} remaining to guess the number.")
    guessed_number=input(int("guess a number:"))
    attempts=check_answer(guessed_number,answer,attempts)