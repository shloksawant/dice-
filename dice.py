import random

user = input("press D to roll the dice")

if user == "d":
    a = random.randint(1,6)
    print(f"{a} is the dice number.")
else:
    print("please enter D to roll the dice")
