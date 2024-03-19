def user_choice(question, valid_list):

    # error code
    error = "Please choose a valid input."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"{error}\n")


# Main routine
yes_no_list = ['yes', 'no']  # List of choices for yes/no questions

see_instructions = ""
while see_instructions != "xxx":

    # ask user for choice, check if its valid
    see_instructions = user_choice("Would you like to see the instructions? ", yes_no_list)

    # print output
    if see_instructions == "xxx":
        break
    elif see_instructions == "yes":
        print("Display Instructions")
    else:
        print("Program Continues")
