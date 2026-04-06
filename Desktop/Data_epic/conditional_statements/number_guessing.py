# guess game using while loop
secret_number = 10

while True:
    guess = int(input("guess a number between 1 and 10: "))
    if guess == secret_number:
        print("correct!!!")
        break
    else:
        print("Incorrect")
