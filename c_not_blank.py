# function goes at top

# function checks that the users input is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this can't be blank or contain only spaces. Please try again")
        else:
            return response


# main routine goes here

while True:
    name = not_blank("What is your name? ")

    if name == "xxx":
        break

    print(f"You entered {name}")