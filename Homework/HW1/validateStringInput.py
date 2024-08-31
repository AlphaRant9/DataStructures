"""
    File:  validateStringInput.py
    Description:  Simple program to demonstrate how to validate
    user-input string is one of a set of strings.   
"""

def main():
    validStringsList = ['a', 'b', 'c']
    validString = getValidString(validStringsList)
    print("The valid string returned in " + str(validStringsList) + " was",validString)


def getValidString(validStringsList):
    """ Repeatedly prompts the user for a valid string from the validStringsList
        and returns the valid string when one is entered.
    """
    userInput = input("Please enter "+str(validStringsList)+ ": ").lower()
    while userInput not in validStringsList:
        print("Invalid entry please try again!")
        userInput = input("Please enter "+str(validStringsList)+ " : ").lower()

    return userInput

# Starts main program running
main()
