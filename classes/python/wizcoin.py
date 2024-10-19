
# __init__ = Initializer

class WizCoin:
    def __init__(self, galleons, sickles, knuts): #parameter):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        # Parameters do not automatically get assigned to the objects
        # The assignment below is what assigns the passed in arguments as attributes of the class
        # A method always has the self parameter. If self is not needed, then code should be a function. 
        # __init__ is not required in class, but almost always present. 
        self.galleons = galleons # Attributes
        self.sickles  = sickles
        self.knuts    = knuts
        # NOTE: __init__() methods NEVER have a return statement.

    def value(self):
        """The value (in knuts) of all the coins in this WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
    
    # Personal Modifications
    def try_new(self):
        """Example of defining a function with an certain attribute. Then assign the attribute later"""
        return self.new_string
    
    def new_number(self):
        """Example of defining a function with an certain attribute. Then assign the attribute later"""
        return self.new_num    