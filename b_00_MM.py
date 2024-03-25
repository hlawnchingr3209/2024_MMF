import pandas


# checks for valid integer input from user
def num_checker(question):
    while True:

        try:
            number = int(input(question))
            return number

        except ValueError:
            print("Please respond with a sensible integer. Please try again.")
            continue


# checks users input makes sure it is not blank
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


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine
MAX_TICKETS = 30
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

# Lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

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

    if pay_method == "cash":
        surcharge = 0
    else:
        # calculate 5% surcharge if users are paying by credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

# create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print("---- Ticket Data ----")
print()

# output table with ticket data
print(mini_movie_frame)

print()
print("----- Ticket Cost / Profit -----")

# output total ticket sales and profit
print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Profit : ${:.2f}".format(profit))

remaining_tickets = MAX_TICKETS - tickets_sold
if tickets_sold == 3:
    print("Congratulations, you have sold all the available tickets.")
else:
    print(f"You have sold {tickets_sold} ticket{'s' if tickets_sold != 1 else ''}."
          f" There {'are' if remaining_tickets != 1 else 'is'} {remaining_tickets} remaining.")
