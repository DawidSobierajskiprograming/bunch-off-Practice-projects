import random


def Outside_home(Player_name,Player_location):
    print("Outside your home you see your friend Bill and a way to head to the harbour")
    playerchoice = input ("What would you like to do? \n")
    if playerchoice == "Bill":
        f = open(r"Text-based-adventure-game\Friends_lines.txt",)
        Random_number = random.randint(0,5)
        Content = f.readlines()
        reply = Content[Random_number]
        print(reply.replace('blank',Player_name))
        f.close
    elif playerchoice == "harbour":
        print("You make your way to the harbour")
        Player_location = 2
    elif playerchoice == "Where am I":
        print("You are currently Ouseide your home")
    else:
        print("You need to type either Bill or harbour")

def Harbour(Player_name, Player_location):
    print("You have arrived at the harbour, you see there is alot of Comotion as a Large Ship has entered port \n")
    print("You see a Sailour sitting on a bench smokig a pipe and a longshoars man looking at some documents")
    playerchoice = input ("What would you like to do? \n")
    

def main():
    Player_name = input("What is your name? \n")
    print ("aftger waking up, having breakfast and shower you decide to go outside")
    Player_location = 1
    while True:
        if Player_location == 1:
            Outside_home(Player_name, Player_location)
        if Player_location == 2:
            Harbour(Player_name, Player_location)
        if Player_location == 3:
            Market(Player_name, Player_location)
        if Player_location == 4:
            TownHall(Player_name, Player_location)
        if Player_location == 5:
            Barracks(Player_name, Player_location)
    

if __name__ == "__main__":
    main()




 

