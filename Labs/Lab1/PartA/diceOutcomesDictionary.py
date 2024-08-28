"""
File:  diceOutcomes.py
Description:  Rolls two dice 1,000 times to determine the outcome(s) with
the highest percentage.
"""
from random import randint
from num2words import num2words
from word2number import w2n

# Global Constants
DIE_SIDES = 6

def main():
    """ Main program provides an outline of program """
    numberOfRolls = welcomeAndInputRolls()
    mostFrequentRolls, highestCount = calculateFrequentRolls(numberOfRolls)
    displayResults(mostFrequentRolls, highestCount, numberOfRolls)


def welcomeAndInputRolls():
    """ Displays welcome message for the user """
    print("This program rolls two %d-sided dice many times to"
          % DIE_SIDES)
    print("determine the outcome(s) with the highest percentage.")
    print()
    numberOfRolls = int(input("How many times would you like to roll the pair of dice?  "))
    return numberOfRolls

def calculateFrequentRolls(numberOfRolls):
    """Rolls the dice the correct number of times, tallies the outcomes, and
       returns a list of outcomes with highest counts and highest count."""

    # initialize outcomeCounts to all 0s.  The index corresponds to the outcome
    # NOTE:  index positions 0 and 1 are not possible
    outcomeCounts = {}
    for count in range(DIE_SIDES*2-1):
        outcomeCounts[num2words(count+2)] = 0

    rollAndTallyOutcomes(outcomeCounts, numberOfRolls)

    print("\noutcomeCounts:",outcomeCounts)    # For debugging

    highestCount = max(outcomeCounts.values())

    mostFrequentRolls = findOutcomes(outcomeCounts, highestCount)

    print("mostFrequentRolls:", mostFrequentRolls,
          "and highestCount:",highestCount)    # For debugging

    return mostFrequentRolls, highestCount


def rollAndTallyOutcomes(outcomeCounts, numberOfRolls):
    """Rolls the dice the correct number of times and tallies the outcomes 
       in the outcomeCounts list of tallies with the index being the outcome."""
    for i in range(numberOfRolls):
        die1 = randint(1, DIE_SIDES)
        die2 = randint(1, DIE_SIDES)
        outcome = die1 + die2
        outcomeCounts[num2words(outcome)] += 1


def findOutcomes(outcomeCounts, highestCount):
    """Returns a list of outcomes with the highest count."""
    highestNumbers = []
    mostFreqNumStr = ''
    for i in range(len(outcomeCounts)):
        if outcomeCounts[num2words(i+2)] == highestCount:
            highestNumbers.append(i+2)

    if len(highestNumbers) == 1:
        return str(highestNumbers[0])
    elif len(highestNumbers) > 1:
        for i in range(len(highestNumbers) - 1):
            mostFreqNumStr += str(highestNumbers[i])
            if len(highestNumbers) > 2:
                mostFreqNumStr += ', '
            else:
                mostFreqNumStr += ' '
        mostFreqNumStr += f'and {str(highestNumbers[-1])}'
        return mostFreqNumStr
    else:
        return "no most frequent outcome found"


def displayResults(mostFrequentRolls, highestCount, numberOfRolls):
    """ Displays the outcome(s) with the highest percentage"""
    print(f'The highest percentage is %3.1f for outcome(s): {mostFrequentRolls}'
          % (highestCount*100/numberOfRolls), end="")
    print()
    
main()
    
        
    
    


