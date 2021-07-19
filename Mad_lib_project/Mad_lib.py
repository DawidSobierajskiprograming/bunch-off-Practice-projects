

noun =  input("Please enter a random noun: ")

f = open(r"Mad_lib_project\Noungames.txt","r")

for line in f:
    newline = line.replace('blank', noun)
    print (newline)

f.close()