# stores all information collected into this information dictionary
information = {}

# program stops after one user information has been collected
total_tries = 10

# program stops when this is entered
secret_word = "stop"

# stores age category
age_category = []

# a loop that lets the program continously prompt the user to input their information
while len(information) < total_tries:

    # shows user instructions and how to stop the program early
    print("Please enter your information or type stop to end")

    name = input("please enter your name: ")  # tells user to input their name

    if name == secret_word:
        # breaks the loop and ends the prorgam early if user input (name) == stop
        break

    # tells user to enter their age and is converted to an integer
    age = int(input("enter your age: "))

    gender = input("enter your gender: ")  # tells user to input their gender

# the conditional statements below categorizes users into age groups and stores the output in the age_category variable

    if age <= 12:
        age_category = "Child"
    elif age <= 19:
        age_category = "Teen"
    elif age <= 39:
        age_category = "Young adult"
    elif age <= 64:
        age_category = "Middle aged"
    else:
        age_category = "Senior"

# Storing all the data collected from the user into the information dictionary, setting the name as a key and the other
# data as values
    information[name] = [age, gender, age_category]

    print(information)  # the program prints all the data collected.
