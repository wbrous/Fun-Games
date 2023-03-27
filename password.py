####################################
#                                  #
#           Gir0fa#6723            #
#                                  #
#            1. Setup              #
#         2. Get password          #
#             3. Main              #
#            4. Credits            #
#                                  #
####################################

# Setup (leave it how it is).

import time

pass_type = 1
revealed_letters = ""
tries = 0

print("Made by Gir0fa#6723")

# Get passfile. (Create file if needed).

if pass_type == 0:
    with open("pass.txt", "w") as file:
        password = input("Enter new password: ")
        file.write(password)
        exit(f"Set password to {password}")
elif pass_type == 1:
    with open("pass.txt", "r") as file:
        password = file.read()
else:
    exit("ERROR: set pass_type in config to 1!!!")

# Main Code

try:
    for letter in password:

        revealed_letters += letter
        tries += 1

        guess = input(f"Guess #{len(revealed_letters)}? ")

        if guess == password:
            print(f"You got it after {tries} tries. \nThe word was {password}.")
            break
        else:
            print(f"Wrong! Revealed letters are: {revealed_letters}")
except:
    print(
    """
    Made by Gir0fa#6723

    Star this repo or follow him for more!

    Also check out his youtube.
    """
    )
    exit("You Stopped The Code!")

# Credits (please dont remove)

print(
    """
    Made by Gir0fa#6723

    Star this repo or follow him for more!

    Also check out his youtube.
    """
)