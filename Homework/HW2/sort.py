import os

DICT_FILE = "dictionary.txt"
JUMBLE_FILE = "jumble.txt"

def main():
    sortedDict = sortDict(DICT_FILE)
    regularJumble, sortedJumble = sortJumble(JUMBLE_FILE)
    resultStr = compareJumble(sortedDict, regularJumble, sortedJumble)
    print(resultStr)

def compareJumble(sortedDict, regularJumble, sortedJumble):
    """Compares the sorted jumbles to the sorted dictionary and returns what each could be decoded to or that it could
        not be decoded."""
    result = ""
    for jumbleIndex in range(len(sortedJumble)):
        result += f'{regularJumble[jumbleIndex]} '
        if sortedDict.get(str(sortedJumble[jumbleIndex]).lower()) is None:
            result += "could not be unscrabbled!\n"
        else:
            tempResult = sortedDict.get(str(sortedJumble[jumbleIndex]).lower())
            result += f'could be unscrabbled to {tempResult}\n'


    return result

def sortJumble(jumbleFile = "jumble.txt"):
    """Sorts Jumble File lines by character to be compared with the dictionary"""
    if os.path.isfile(jumbleFile):
        jumble = open(jumbleFile)
    else:
        raise FileNotFoundError("Jumble file not found")

    jumbleLines = jumble.readlines()
    regularJumble = []
    sortedJumble = []

    for line in jumbleLines:
        temp = []
        tempStr = ""
        tempSortedStr = ""
        for char in line:
            if char != "\n":
                temp.append(char)

        for char in temp:
            tempStr += char

        regularJumble.append(tempStr)

        temp.sort()

        for char in temp:
            tempSortedStr += char

        sortedJumble.append(tempSortedStr)

    return regularJumble, sortedJumble

def sortDict(dictFile = "dictionary.txt"):
    """Sorts every character alphabetically by line in a file and writes to a new file with the sorted list."""
    original = open(dictFile, "r")
    sortedDict = {}

    for line in original.readlines():
        temp = []
        tempStr = ""
        tempStrSorted = ""
        for char in line:
            if char != "\n":
                temp.append(char)

        for char in temp:
            tempStr += char
        temp.sort()
        for char in temp:
            tempStrSorted += char

        if tempStrSorted not in sortedDict:
            sortedDict[tempStrSorted] = [tempStr]
        else:
            sortedDict[tempStrSorted].append(tempStr)
    return sortedDict

main()