import random
b = input("How many times do you want to roll the dice? ")
for i in range(int(b)):
    print(random.randint(1,6))