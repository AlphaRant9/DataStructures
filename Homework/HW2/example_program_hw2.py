""" Simple program to sort a string's characters. """
myString = "snakes"
print("Original myString:", myString)

myString = myString.upper()  # upper-case the string's letters
print("Upper-case myString:", myString)

listOfLetters = list(myString) # create a list of letters from the string
print("listOfLetters:", listOfLetters)

listOfLetters.sort()  # sorts the list of letters
print("sorted listOfLetters:", listOfLetters)

# join the sorted list of letters back together into a string using an
# empty-string separator between letters
myStringSorted = "".join(listOfLetters) 
print("myString:", myString, "myStringSorted:", myStringSorted)
