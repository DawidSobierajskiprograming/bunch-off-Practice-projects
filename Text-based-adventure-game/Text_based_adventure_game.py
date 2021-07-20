import random
Player_location = 1

def Outside_home(Player_name):
    print("Outside your home you see your friend Bill and a way to head to the harbour")
    playerchoice = input ("What would you like to do? \n")
    if playerchoice == "Bill":
        f = open(r"Text-based-adventure-game\Friends_lines.txt")
        Random_number = random.randint(0,5)
        Content = f.readlines()
        reply = Content[Random_number]
        print(reply.replace('blank',Player_name))
        f.close
    elif playerchoice == "Harbour":
        print("You make your way to the harbour")
        global Player_location
        Player_location = 2
    elif playerchoice == "Where am I":
        print("You are currently Ouseide your home")
    else:
        print("You need to type either Bill or harbour")

def Harbour(Player_name):
    print("You have arrived at the harbour, you see there is alot of Comotion as a Large Ship has entered port \n")
    print("You see a Sailour sitting on a bench smokig a pipe and a longshoars man looking at some documents\n")
    print("You know that if you head north from the harbour you will get to the market square")
    playerchoice = input ("What would you like to do? \n")
    if playerchoice == "Sailour":
        f = open(r"Text-based-adventure-game\Sailour_lines.txt")
        Random_number = random.randint(0,2)
        Content1 = f.readlines()
        reply = Content1[Random_number]
        print(reply.replace('blank',Player_name))
        f.close
    elif playerchoice == "longshores man":
        f = open(r"Text-based-adventure-game\Harbour_man_lines.txt")
        Random_number = random.randint(0,3)
        Content = f.readlines()
        reply = Content[Random_number]
        print(reply.replace('blank',Player_name))
        f.close
    elif playerchoice == "Where am I":
        print("You are currently at the harbour")
    elif playerchoice == "Market":
        print("You make your way to the market square")
        Player_location = 3
    elif playerchoice == "Home":
        print("You go along a path heading east to get back home")
        Player_location = 1
    else:
        print("You need to type either Bill or harbour")

def main():
    Player_name = input("What is your name? \n")
    print ("aftger waking up, having breakfast and shower you decide to go outside")
    while True:
        print(Player_location)
        if Player_location == 1:
            Outside_home(Player_name)
        if Player_location == 2:
            Harbour(Player_name)
        if Player_location == 3:
            Market(Player_name)
        if Player_location == 4:
            TownHall(Player_name)
        if Player_location == 5:
            Barracks(Player_name)
        print(Player_location)

if __name__ == "__main__":
    main()




 

