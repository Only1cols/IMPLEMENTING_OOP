# password prompt
password = "Okeke123"

while True:
    user_input = input("Input your password: ")
    if password == user_input:
        print("correct password")
        break
    else:
        print("Password incorrect")
