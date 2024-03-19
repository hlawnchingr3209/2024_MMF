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


yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for i in range(0, 5):
    wait_instructions = string_checker("Do you want to read the instructions (y/n): ", yes_no_list, 1)
    print(f"You chose {wait_instructions}")

for i in range(0, 5):
    pay_method = string_checker("Payment method: ", payment_list, 2)
    print("You chose", pay_method)