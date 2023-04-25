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

pass_type = 1 # Change to "0" if u wanna change password.
revealed_letters = "" # Don't change. It is for the revealing letters. Line 49.
tries = 0 # For stopping code once u run out of guesses.

print("Made by Gir0fa#6723") # Credits

# Get passfile. (Create file if needed).

if pass_type == 0: # check var from line 16
    with open("pass.txt", "w") as file: # open file
        password = input("Enter new password: ") # ask for pass
        file.write(password) # write pass
        exit(f"Set password to {password}") # confirmation
elif pass_type == 1: # check var
    with open("pass.txt", "r") as file: # read file
        password = file.read() #define local var from text
else:
    exit("ERROR: set pass_type in config to 1!!!") # if error

# Main Code

try: # if error
    for letter in password: # for loop

        revealed_letters += letter # some math
        tries += 1 # more math

        guess = input(f"Guess #{len(revealed_letters)}? ") # ask for guess

        if guess == password: # if guess is pass
            print(f"You got it after {tries} tries. \nThe word was {password}.")
            break
        else:
            print(f"Wrong! Revealed letters are: {revealed_letters}")
except: # run if error
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
