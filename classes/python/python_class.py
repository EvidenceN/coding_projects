# Things I want to cover. 
# The concept of Init. Understand how it works, how to utilize it,
# Understand methods, relationship between init in class and it's methods
# Understand class instance initiation in relationship to init and methods

# Class Lessons

# class student ():
"""
OOP with Python - https://inventwithpython.com/beyond/chapter15.html

OOP with Inheritance in Python - https://inventwithpython.com/beyond/chapter16.html

OOP & dunder methods in Python - https://inventwithpython.com/beyond/chapter17.html



"""    

import datetime # datetime is a module
birthday = datetime.date(1999, 10, 31) # datetime.date is the class within that module
birthday.year # datetime.date.year is an attribute of the date class object 
birthday.month # Attribute as well. But this attribute is "read-only" according to the docs.
birthday.day
birthday.weekday() # weekday() is a method within the datetime.date object.