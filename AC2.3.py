
# AC 2.3 - Git Version Control Practice

def welcome_user():
    name = input("Enter your name: ")
    print("Welcome", name)


def check_voting_age(age):
    """Check whether the user is old enough to vote."""
    minimum_voting_age = 18
    return age >= minimum_voting_age


welcome_user()

while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Please enter a valid age.")
            continue

        break

    except ValueError:
        print("Please enter your age as a whole number.")

if check_voting_age(age):
    print("You are eligible to vote.")
else:
    print("You are not yet eligible to vote.")




# This program practises Python functions and Git version control.



# Temporary change for practising commit deletion.

