import  sys
import keyword
import operator
from datetime import datetime
import os

# keyword
    # Keywords are the reserved words in Python and can't be used as an identifier.
print(keyword.kwlist)
print(len(keyword.kwlist))

print('*'*40)
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

print('*'*40)


# Statements
    # Instructions that a Python interpreter can execute.
    # single line statements
p1 = 10 + 20
print ('p1:',p1)
    #multi line statements
p2 = 20  \
    + 40 # there is differece between \ and /
# \ use for show the next line, dosent mean anything
p3 = 20 / 40
print(p2)
print ('p3 = 20 / 40 = ',p3)

print('*'*40)

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

print('*'*40)

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
     # r,p,q point to the same location that is location of '30'.

# Variable Assigment # python is dynamic type. it detect type of variable by itself.
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

print('*'*40)

# Boolean
    # Boolean data type can have only two possible values true or false.
bool1 = True
print(type(bool1))
print(bool(0))
print(bool(1))

print('---------------------------')
print('---------------------------')

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

print('*'*40)

# String Indexing
print(mystr2[0])    # First character in string "str1"
print(mystr2[-1])   # Last character in string

print('---------------------------')


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
str1 = 'hello'
for char in str1:
    print(char)
print(enumerate(str1))
print(type(enumerate(str1)))
print(list(enumerate(str1)))
    # Enumerate method adds a counter to an iterable

print('---------------------------')
# check String Membership
mystr1 = 'hello everyone'
print('hel' in mystr1) #-----TRUE --- SEARCH PART OF IT IS ALSO TRUE
print('hello' in mystr1)  #----TURE

# String Partitioning :
    #   The partition() method searches for a specified string and
    #   splits the string into BEFORE STR, STR , AFTER STR
str5 = "Natural language and R and Java"
L = str5.partition("and")
print(L)

print('-----------------------------')
## OTHER STRING FUNCTION:
mystr2= "   *****He HeLLO * each****   "
a= mystr2.strip()
print(mystr2)
print('mystr2.strip(): ',a)
print(mystr2.rstrip()) # Removes all whitespaces at the end of the string
print(mystr2.lstrip()) # Removes all whitespaces at the begining of the string
print('strip:', mystr2.strip()) # strip() = Removes white space from begining & end
print('strip *:', mystr2.strip('   *')) # Removes all '*' characters from begining & end of the string
print('lower:', mystr2.lower()) # Return whole string in lowercase
print(mystr2.upper()) # Return whole string in uppercase
print('replace:' , mystr2.replace("He" , "Ho")) #Replace substring "He" with "Ho"
print('replace * with ' ' :' , mystr2.replace("*" , "")) #Replace substring "*" with ""
    # در دستور replace هم مثل دستور in عمل میکنه. یعنی عین کلمه را دنبالش نمی گرده. اگر بخشی از کلمه هم مطابقت داشته باش، تغییر میده.

#### نکته : من فکر میکردم خود "متن" بعد از دستور تغییر میکنه. ولی نمی کنه.
#### یا باید بعد از دستور با "=" به یه متغیر جدید مربوط کنیم یا مستقیم داخل "print" بزاریم.

print('-----------------------------')

mystr5 = "one two Three one two two three"
print(mystr5.count("one")) # count: count Number of times substring "one" occurred in string.

mylist = mystr5.split() # Split: Split String into substrings in list
print(mylist)

print('-----------------------------')
##checking alpha,numeric and ...
mystr6 = 'abc123456789'
print(mystr6.isalpha()) # returns True if all the characters in the text are letter
print(mystr6.isalnum()) # returns True if a string contains only letters or number
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric()) # returns True if all the characters are numeric (0-9
print(mystr6.isupper()) # Returns True if all the characters are in upper case
print(mystr6.islower()) # Returns True if all the characters are in lower case
print(mystr5.rfind("one")) # Returns index of last occurrence of word 'one' in string "str6"
print(mystr5.rindex("one")) # Returns index of last occurrence of word 'one' in string "str6"























