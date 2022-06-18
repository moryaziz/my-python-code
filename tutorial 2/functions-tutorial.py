#Functions
# A function is a block of organized code written to carry out a specified task.
# Functions help break our program into smaller and modular chunks for better readability.
# Information can be passed into a function as arguments.
# Parameters are specified after the function name inside the parentheses.
# We can add as many parameters as we want. Parameters must be separated with a comma.
# A function may or may not return data.
# In Python a function is defined using the def keyword

# Parameter VS Argument
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Three types of functions in Python:-
# Built-in function :- Python predefined functions that are readily available for use
    # like min() ,max() , sum() , print() etc. there are 63 functions.
# User-Defined Functions:- Function that we define ourselves to perform a specific task.
# Anonymous functions : Function that is defined without a name.
    # Anonymous functions are also called as lambda functions. They are not declared with the def keyword

def FunctionName (parameters):
    """Function DosString"""
    statements
    return [expression]

#calling function :
a = 'salam'
#FunctionName(a)

def myfunc():
    print('salam python')
myfunc()

def details(name,userid,country):
    """Function to print User details"""
    print('Name :- ', name)
    print('User ID is :- ', userid)
    print('Country :- ',country)

details('mory' , '22' , 'iran')

def square (n):
    """function to find square of a number"""
    n = n**2
    return n

square (10) # it does not print anything, it retrun amount of number
print(square(10))
a = square (10)
print(a)

def even_odd (num): #Even odd test
    """ This function will check whether a number is even or odd"""
    if num % 2 ==0:
        print (num, ' is even number')
    else:
        print (num, ' is odd number')

even_odd(3)
even_odd(4)
print(even_odd.__doc__) # Print function documentation string

print('-----------------------------')

def fullname (firstname , middlename ,lastname): #Concatenate Strings
    """parameters : firstname , middlename ,lastname """
    fullname = "{} {} {}".format(firstname,middlename,lastname)
    print (fullname)

print(fullname.__doc__)
fullname(lastname = 'aziz' , middlename='-' , firstname='mory')
    # Keyword Arguments

#fullname (lastname = 'aziz') # This will throw error as function is expecting 3 arguments.


# define 'default value' for Function may be useful
def city_of_birth(city = 'tehran'):
    print('Most Populous City :- ', city)

city_of_birth() # When a function is called without an argument it will use default valu
city_of_birth('tabriz')

print('-----------------------------')

# Global and local scope variable
var1 = 100 # Variable with Global scope.
def myfunc():
    print(var1) # Value 100 will be displayed due to global scope of var1
myfunc()

def myfunc1():
    var2 = 10 # Variable with Local scope
    print(var2)
myfunc1()

def myfunc2():
    print(var2)
# myfunc2() # This will throw error because var2 has a local scope.
    # var2 is local variable for myfunc1.

print('-----------------------------')

var1 = 100 # Variable with Global scope.
def myfunc():
    var1 = 99 # Local scope
    print(var1)
myfunc()
print(var1) # The original value of var1 (100) will be retained and unchanged due to global scope.
    # you cant change the value of Global scope in a function


var1 = 100 # Variable with Global scope.
def myfunc(var2):
    #int(var2)
    var1 = var2 # Local scope
    print(var1)
myfunc(20)
print(var1) # The original value of var1 (100) will be retained and unchanged due to global scope.
    # you cant change the value of Global scope in a function











