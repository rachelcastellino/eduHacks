def choosePath():
    output = input("Thanks for choosing [need to fill] to [need to fill]. Please enter whether you want to (1) Score Your Email (2) Push Your Syllabus or (3) Draft an Email: ")
    if output == int(1):
        challenge()

    if output == int(2):
        syllabus()

    else:
        draft()

def challenge():
    print("You chose Challenge. We will give you a variety of prompts and you will draft an email in under 350 words. We will then give you a score on how well your email is written and meets the purpose.")
    print("Prompt 1: Write an email to an old colleague to ask them more about the work they are doing and how they like it at their company.")
    email = input("")
    print("Prompt 2: Write an email to a company asking about an out of stock item you have been wanting to buy. Mention you have a discount coupon and if that can be applied.")
    email = input("")
    print("Promtp 3: Write an email inviting your friends to a holiday party. Make sure you mention if it is a potluck and who needs to bring what.")
    email = input("")

def syllabus():
    print("You chose to push your syllabus.")

def draft():
    print("You chose to draft your email. Please follow the prompts to enter the appropriate information. A sample of different emails will be outputted.")
    name = input("Please enter your name: ")
    receiver = input("Please enter the email of the person you are writing the email to: ")
    greeting = input("Please choose a greeting (1) Hi or Hello (2) Good Morning / Afternoon / Evening (3) Dear (4) To Whom it May Concern: ")
    purpose = input("Please enter the purpose of your email: ")

