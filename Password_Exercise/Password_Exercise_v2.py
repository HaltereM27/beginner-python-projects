# Solicita ao usuário para criar uma senha
password = input("Please, enter a word to create a password: ")
print("Great, now let's login in your account...")

# Variável para armazenar a senha digitada pelo usuário durante o login
entered_password = ''

# Loop até que a senha correta seja digitada
while entered_password != password:
    entered_password = input("Please, enter the correct password: ")
    if entered_password == password:
        print("Welcome!")
    else:
        print("Sorry, the password you entered is incorrect. Try again.")
