import math
from random import randint

def main():
    print("Welcome to the Math Tutor\n")
    name = input("Enter your name: ")
    grade = getValidInt("Enter your grade (1, 2, or 3): ",
                        "Enter a valid grade (1, 2, or 3).",
                        1, 3)
    print(f'\nDirections:  Please answer the following 5 problems {name}.\n')
    correct = promptProblems(name, grade)
    print(f'\n{"="*16} Summary {"="*16}')
    print(f'Bye {name}! You answered {correct} out of 5 correct.')

def getValidInt(prompt, error = "Enter a valid integer", minValue = -math.inf, maxValue = math.inf):
    """ Repeatedly prompts the user for a valid integer
        and returns the valid integer when one is entered.
    """
    while True:
        try:  # tries to convert input string to an int and ensure it is within the set bounds
              # but if it fails do "except" code; otherwise break out of the loop
            grade = int(input(prompt))
            if minValue <= grade <= maxValue: # only gets here if the conversion to an int was successful
                return grade
            else:
                return ValueError(error)

        except:
            print(error)


def promptProblems(name, grade):
    """Prompts the user with 5 math problems, then returns the number of problems the user got correct"""
    correct = 0
    if grade == 1:
        min = 0
        max = 9
    elif grade == 2:
        min = 10
        max = 99
    else:
        min = 100
        max = 999
    for i in range(5):
        value1 = randint(min, max)
        value2 = randint(min, max)
        print(f'Problem #{i + 1}:  {value1}')
        print(f'           + {value2}')
        print(f'            ____')
        answer = value1 + value2
        if answer == getValidInt("Answer: "):
            print(f'\nGreat {name}, your answer is correct!\n')
            correct += 1
        else:
            print(f'\nSorry {name}, your answer is incorrect. The correct answer is {answer}')
    return correct

main()