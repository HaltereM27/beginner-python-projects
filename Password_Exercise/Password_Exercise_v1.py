#While Loops - EXERCISE
#Program that uses a while loop to test user input of a secret password.

password = " "
while password != "secret":
    password = input("Please enter the password: ")
    if password == "secret":
        print("Welcome!")
    else:
        print("Sorry, the password you entered is incorect. Try again.")

