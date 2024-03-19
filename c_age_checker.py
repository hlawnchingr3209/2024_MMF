# functions go here
def num_checker(question):

    while True:

        try:
            age = int(input(question))
            return age

        except ValueError:
            print("Please respond with a sensible integer. Please try again.")
            continue


# Main routine goes here
tickets_sold = 0

while True:

    name = input("\nWhat is your name? ")

    if name == "xxx":
        break

    age = num_checker("What is your age? ")

    if 10 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("This looks like it may be a typo, please try again.")
        continue


    tickets_sold += 1

print(f"You have sold {tickets_sold} tickets")