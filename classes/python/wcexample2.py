import wizcoin

change = wizcoin.WizCoin(9, 7, 20)
print(change.sickles) # Prints 7.
change.sickles += 10
print(change.sickles) # Prints 17.

pile = wizcoin.WizCoin(2, 3, 31)
print(pile.sickles) # Prints 3.
pile.someNewAttribute = 'a new attr' # A new attribute is created.
print(pile.someNewAttribute)

# Example of defining a function with an certain attribute. Then assign the attribute later
# These are the attributes
pile.new_string = 'A BRAND NEW STRING'
print(pile.try_new())

pile.new_numbers = 5 #change to new_num to work
print(pile.new_number())


# Technically, methods are considered attributes of a class, as well.
# Anything after the . is an attribute

