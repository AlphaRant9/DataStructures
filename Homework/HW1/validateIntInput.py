"""
    File:  validateIntInput.py
    Description:  Simple program to demonstrate try-except to validate
    an integer input from the user.   
"""

def main():
    prompt = "Please enter an integer value: "
    validInt = getValidInt(prompt)
    print("The integer returned was",validInt)

def getValidInt(prompt):
    """ Repeatedly prompts the user for a valid integer 
        and returns the valid integer when one is entered.
    """
    while True:
        try:  # tries to convert input string to an int, but if it fails
              # do "except" code; otherwise break out of the loop
            number = int(input(prompt))
            break  # only gets here if the conversion to an int was successful
        except:
            print("Invalid integer! Please retry.")

    return number

# Starts main program running
main()
