
# checks for valid integer input from user
def num_checker(question):
    while True:

        try:
            number = int(input(question))
            return number

        except ValueError:
            print("Please respond with a sensible integer. Please try again.")
            continue


# checks users input makes sure it isnt blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this can't be blank or contain only spaces. Please try again")
        else:
            return response


# calculate the ticket price based on the age
def calc_ticket_price(var_age):

    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# checks if user input is valid based on list and acceptable num_letters.
def string_checker(question, valid_list, num_letters):
    # error code
    error = f"Please choose either '{valid_list[0]}' or '{valid_list[1]}'."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for item in valid_list:
            if response == item[:num_letters] or response == item:
                return item

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"{error}\n")


# main routine
MAX_TICKETS = 30
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

# loop to sell tickets
tickets_sold = 0

# ask user if they want to see the instructions
want_instructions = string_checker("Do you want to read the instructions? ", yes_no_list, 1)

if want_instructions == "yes":
    print("Display Instructions")

while tickets_sold < MAX_TICKETS:

    # makes sure that name is not blank from user input
    name = not_blank("\nWhat is your name? ")

    # exit code
    if name == "xxx":
        break

    # makes sure users input is a valid number
    age = num_checker("What is your age? ")

    # makes sure it is between 12 and 120
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("This looks like it may be a typo, please try again.")
        continue

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)

    # get payment method
    pay_method = string_checker("Choose a payment method (cash/ credit): ", payment_list, 2)
    print("pay method", pay_method)

    tickets_sold += 1

remaining_tickets = MAX_TICKETS - tickets_sold
if tickets_sold == 3:
    print("Congratulations, you have sold all the available tickets.")
else:
    print(f"You have sold {tickets_sold} ticket{'s' if tickets_sold != 1 else ''}."
          f" There {'are' if remaining_tickets != 1 else 'is'} {remaining_tickets} remaining.")
