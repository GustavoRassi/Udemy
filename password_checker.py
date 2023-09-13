username = input("What is your username? \n> ")
password = input("What is your password? \n> ")

hidden_password = '*' * len(password)
password_length = len(password)

print(f"{username}, your password {hidden_password} is {password_length} letters long.")