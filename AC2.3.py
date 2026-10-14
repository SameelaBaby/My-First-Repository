
#AC 2.3 - Git Version Control Practice

def welcome_user():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print("Welcome", name)

    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not yet eligible to vote.")


welcome_user()   




# AC 2.3 - Git Version Control Practice

def welcome_user():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print("Welcome", name)

    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not yet eligible to vote.")


welcome_user()





def welcome_user():
    name = input("Enter your name: ")
    print("Welcome", name)


def check_voting_age(age):
    return age >= 18


welcome_user()

age = int(input("Enter your age: "))

if check_voting_age(age):
    print("You are eligible to vote.")
else:
    print("You are not yet eligible to vote.")
