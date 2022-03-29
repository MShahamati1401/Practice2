import random

dice = (1, 2, 3, 4, 5, 6)

while True:
    x = int(input("Guess Number , For exit typed exit"))
    y = random.choice(dice)
    if x == y or y == 6:
        print("YOU WINNER")
    else:
        print(f"number choice by system = {y}")
        print("YOU LOSER")
        break