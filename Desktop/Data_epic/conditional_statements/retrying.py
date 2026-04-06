# password prompt

password = "Okeke123"

while True:
    user_input = (input("Please enter your password: "))
    if password == user_input:
        print("Password correct")
        break
    else:
        user_input != password
        print("Password is incorrect, try again")
