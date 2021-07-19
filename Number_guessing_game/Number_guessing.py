import random

def Main():
    print("Welcome to the Random number Guessing Game ")


    Game_iteration = 0
    Game_number = random.randint(0,100)
    print(Game_number)
    while True:
     
        userinput = int(input("Please enter your guess:"))
    
        if userinput == Game_number:
            print("You guessed the number " + str(Game_number) + " Correctly")
            print("YOU WIN")
            input()
            break
        else:
            print("You guessed wrong")
            print("Please Guess again")
            Game_iteration += 1
            if Game_iteration == 5 or Game_iteration >= 5:
               print("The correct anwser is " + str(Game_number))
               print("GAME OVER")
               input()
               break
            else:
                Bigger_or_smaller(Game_number)

def Bigger_or_smaller(Game_number):
    anchor = None
    while anchor == Game_number or anchor == None:
        anchor = random.randint(0,100)
    if Game_number > anchor:
        print("The game number is greater than " + str(anchor))
    if Game_number < anchor:
        print("The game number is less than " + str(anchor))




Main()