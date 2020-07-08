from random import randint

class Die():
    """ A class for a single die."""

    def __init__(self, numSides=6):
        """Default to six sided die."""
        self.numSides = numSides

    def roll(self):
        """Return a random value from 1 to number of sides."""
        return randint(1, self.numSides)