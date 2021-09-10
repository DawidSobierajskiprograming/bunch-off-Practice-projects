

email = input("Please Input the email: ")
if email.find("@") > 0:
    splitemail = email.split("@")
    print(" The username of the email is: " + str(splitemail[0] + " The Domain of the email is: " + str(splitemail[1])))
else:
    print("Please Input a real email address")