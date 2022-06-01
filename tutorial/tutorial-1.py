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

# Variables
'''
id() function returns the “identity” of the object. 
The identity of an object - Is an integer
 - Guaranteed to be unique
 - Constant for this object during its lifetime. 
'''
    # hex(id(p))    # Memory address of the variable
p = 30
print(p , type(p) , hex(id(p)))
r = 30
print(r , type(r) , hex(id(r)))
q = p
print(q , type(q) , hex(id(q)))
     # variable q will also point to the same location where p and r are pointing

# Variable Assigment
intvar = 10     # Integer variable
floatvar = 2.57     # Float Variable
strvar = "Python Language"      # String variable
print(intvar)
print(floatvar)
print(strvar)
# Multiple Assignments
intvar , floatvar , strvar = 10,2.57,"Python Language"
    # Using commas to separate


#Data Types
val1 = 10   # Integer data type
val2 = 92.78    # Float data type
val3 = 25 + 10j # Complex data type

print(val1)
print(type(val1))   # type of object
print(sys.getsizeof(val1))  # size of integer object in bytes
print(val1, " is Integer?", isinstance(val1, int)) # is val1 an int? True
print(val1, " is Integer?", isinstance(val1, float)) # is val1 an int? True


# Boolean
    # Boolean data type can have only two possible values true or false.
bool1 = True
print(type(bool1))
print(bool(0))
print(bool(1))

# Strings
mystr = 'Hello World' # Define string using single quotes
print(mystr)
mystr = "Hello World" # Define string using double quotes
print(mystr)
mystr = '''Hello World ''' # Define string using triple quotes
print(mystr)
mystr2 = 'Woohoo'*5
print(mystr2)

print(len(mystr2))    # Length of string

# String Indexing
print(mystr2[0])    # First character in string "str1"
print(mystr2[-1])   # Last character in string


# String Slicing
str1 = 'hello'
print(str1[0:3:2])  #  [start:end:step]

# String concatenation
s1 , s2 = 'hello','ali'
s3=s1+s2
s4=s1+' '+s2
print(s1,s2)
print(s3)
print(s4)

# Iterating through a String
for char in str1:
    print(char)
print(enumerate(str1))
print(type(enumerate(str1)))
print(list(enumerate(str1)))
    # Enumerate method adds a counter to an iterable























