import  sys
import keyword
import operator
from datetime import datetime
import os

# keyword
    # Keywords are the reserved words in Python and can't be used as an identifier
print(keyword.kwlist)
print(len(keyword.kwlist))

# identifiers
    # An identifier is a name given to entities like class, functions, variables, etc.
    # It helps to differentiate one entity from another

# val2@ = 35        # Identifier can't use special symbols
#import = 25        # Keywords can't be used as identifiers
 #two way of defining identifier
 # val_of_imo
 # ValOfImo


# comments in python code
    #Comments can be used to explain the code for more readabilty.

# Indentation:
# Indentation refers to the spaces at the beginning of a code line
# الکی فاصله بزاری ارور میده
    #p1 = 10 + 20  #IndentationError: unexpected indent




# Statements
    # Instructions that a Python interpreter can execute.
    # single line statements
p1 = 10 + 20
print (p1)
    #multi line statements
p2 = 20  \
    + 40 # there is differece between \ and /
# \ use for show the next line, dosent mean anything
p3 = 20 / 40
print(p2)
print (p3)

# Docstrings
    #1) Docstrings provide a convenient way of associating documentation with
    #functions, classes,methods or modules.
    #2) They appear right after the definition of a function, method, class, or module.
    # اگر یک تابع یا ماژول تعریف کردیم و خواستیم برای کسی که کد رو اجرا میکنه بدونه این کد چکار میکنه
def square(num):
    '''square function: this function will return square number'''
    return num**2
print (square(2))
# # We can access the Docstring using __doc__ method
print(square.__doc__)