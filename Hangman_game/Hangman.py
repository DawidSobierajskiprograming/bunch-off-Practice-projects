import random


words = ("list","child","pan","number","dog","sea","slime","dollar")
word = words[random.randint(0, len(words)-1)]
goes = 0
print("You have 10 lives to guess the word")
while goes < 10:
    b = input("Please enter a letter or word ")
    if b == word:
        print("YOU WIN")
        print("The word was: " + word)
    elif b in word:
        x = word.count(b)
        print("The letter: " + b + " is in the word")
        print("The letter apears " + str(x) + " number of times in the word")
    else:
        print("You are wrong -1 life")
        goes =+ 1