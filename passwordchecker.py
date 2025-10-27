#password checker
storage = {}

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    storage[username] = password
    print("Registration successful!")

def login():
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    if input_username in storage and storage[input_username] == input_password:
        print("Login successful!")
    else:
        print("Login failed!")

condition = True
while True:
    print("Welcome! What would you like to do?")
    print("1. Register")
    print("2. Login")
    answer = (input("Enter 1 or 2: "))

    if answer == "1":
        register()
    elif answer == "2":
        login()
    else:
        condition = False
        print("Exiting the program.")
        break


