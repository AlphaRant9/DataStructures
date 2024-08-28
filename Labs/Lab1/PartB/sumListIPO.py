""" Simple IPO program to sum a list of numbers. """
def main():
    label, values = getInput()
    total = sum(values)
    displayResults(label, total)
    
def getInput():
    """ Get label and list of values to sum."""
    label = input("What are we summing? ")
    numberOfValues = getValidInt("How many values are there? ")
    values = []
    for i in range(numberOfValues):
        # MODIFY below line to call your getValidNumber function
        values.append(getValidNumber("Enter the next number: "))
    return label, values

def getValidInt(promptStr):
    """Repeatedly prompts the user to enter a valid integer until one is
       entered correctly, then it's value is returned.
    """
    while True:   # repeat "forever" or until return valid myInt from function
        try: # try to do int conversion, but if it fails do except code
            myInt = int(input(promptStr))   
            return myInt  # only return if int conversion is successful
        except:
            print("Invalid integer entered! Please try again use only digits (e.g., 123)")

def getValidNumber(promptStr):
    """Repeatedly prompts the user to enter a valid number until one is
       entered correctly, then it's value is returned.
    """
    while True:   # repeat "forever" or until return valid myInt from function
        try: # try to do int conversion, but if it fails do except code
            myFloat = float(input(promptStr))
            return myFloat  # only return if int conversion is successful
        except:
            print("Invalid number entered! Please try again use only digits and at most one period (e.g., 123, 2.2)")

def displayResults(label, total):
    """ Display sum of values. """
    print("The sum of", label, "values is", total)

main() # starts the main function running AFTER loading function definitions

