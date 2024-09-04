from multiprocessing.managers import Value

from advanced_die import AdvancedDie


class MoreAdvancedDie(AdvancedDie):
    """Class based on AdvancedDie to add the functionality of manually setting the roll.
       This is useful for troubleshooting possible end cases of the die roll.
    """
    def __init__(self, sides = 6):
        super().__init__(sides)

    def setRoll(self, roll):
        """Checks the input to see if it is a valid roll (integer between 1 and _numSides) and if it is valid,
           Sets the roll to whatever number is input.
        """
        _roll = self.getValidRoll(roll) # Verify the roll input is a valid roll
        self._currentRoll = _roll # Only gets to this point if the roll is valid


    def getValidRoll(self, _input):
        """ inputs anything and returns a valid roll between bounds
            or raises an error for it being out of bounds or an invalid integer.
        """
        while True:
            try:  # tries to convert input string to an int, but if it fails
                  # do "except" code; otherwise break out of the loop
                number = int(_input)
                if 1 <= number <= self._numSides:
                    return number # only gets to this point if an integer between 1 and _numSides was entered
                else:
                    raise ValueError("Roll out of bounds.") # user input an integer that is outside our die's
                                                            # possible rolls
            except:
                raise TypeError("Invalid integer.") # user did not input an integer
