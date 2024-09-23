import os

sortedDict = {}
sortedJumble = []

def main():
    sortDict()
    sortJumble()

def sortJumble(jumbleFile = "jumble.txt"):
    """Sorts Jumble File lines by character to be compared with """
    if os.path.isfile(jumbleFile):
        jumble = open(jumbleFile)
    else:
        raise FileNotFoundError("Jumble file not found")

    jumbleLines = jumble.readlines()

    for line in jumbleLines:
        temp = []
        tempStr = ""
        for char in line:
            if char != "\n":
                temp.append(char)

        temp.sort()

        for char in temp:
            tempStr += char

        sortedJumble.append(tempStr)




def sortDict(dictFile = "dictionary.txt"):
    """Sorts every character alphabetically by line in a file and writes to a new file with the sorted list."""
    original = open(dictFile, "r")
    global sortedDict

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

main()