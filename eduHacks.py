def choosePath():
    output = input("Thanks for choosing [need to fill] to [need to fill]. Please enter whether you want to (1) Score Your Email (2) Push Your Syllabus or (3) Draft an Email: ")
    if output == int(1):
        challenge()

    if output == int(2):
        syllabus()

    else:
        draft()

def challenge():
    print("You chose to score your email. Please follow the prompts to enter your email purpose and email text. A score and feedback will be outputted.")
    purpose = input("Please type in your email purpose: ")
    email = input("Please enter your email text: ")

def syllabus():
    print("You chose to push your syllabus.")

def draft():
    print("You chose to draft your email. Please follow the prompts to enter the appropriate information. A sample of different emails will be outputted.")
    name = input("Please enter your name: ")
    receiver = input("Please enter the email of the person you are writing the email to: ")
    greeting = input("Please choose a greeting (1) Hi or Hello (2) Good Morning / Afternoon / Evening (3) Dear (4) To Whom it May Concern: ")
    purpose = input("Please enter the purpose of your email: ")

