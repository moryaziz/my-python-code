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
# def adder(a---> parameter)
# sumof = adder(4----> argument)

# Three types of functions in Python:-
# Built-in function :- Python predefined functions that are readily available for use
    # like min() ,max() , sum() , print() etc. there are 63 functions.
# User-Defined Functions:- Function that we define ourselves to perform a specific task.
# Anonymous functions : Function that is defined without a name.
    # Anonymous functions are also called as lambda functions. They are not declared with the def keyword

# print function: perform 2 job:
# if it is possible: convert the export to 'str' and print it.
# if not possible: print the 'temp address' of the function.

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

# fullname (lastname = 'aziz') # This will throw error as function is expecting 3 arguments.


# define 'default value' for Function may be useful
def city_of_birth(city = 'tehran'):
    print('Most Populous City :- ', city)

city_of_birth() # When a function is called without an argument it will use default value.
city_of_birth('tabriz')

print('-----------------------------')

print('Global and local scope variable')

# ****** Global and local scope variable
# global scope : the parameter that be defined in the module.
# local scope : the parameter that be defined in the function.
# we can't use local variable out of the function.
# we can use global variable but can't change amount of the global variable in function except when we define it:
# in the body of function: global ...........


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

print('-----------------------------')

list1 = [11,22,33,44,55]
def myfunc(list1):
    del list1[0]
    list1.append(66)
print('"List1" before calling the function:- ',list1)
myfunc(list1)   # Pass by reference (Any change in the parameter within the function.
print('"List1" after calling the function:- ',list1)

list1 = [11,22,33,44,55]
def myfunc(list1):
    list1 = [11,100,1000,10000,12] # link of 'list1' with previous object is broken
print('"List1" before calling the function:- ',list1)
myfunc(list1) # Pass by reference (Any change in the parameter within the functi
print('"List1" after calling the function:- ',list1)

### you can del or add member to the list and tuple from def (change global list and tuple from local scope)
### but you cant replace all of list and tuple with another value.


def swap(a,b):
    temp = a
    a = b # link of 'a' with previous object is broken now as new object is
    b = temp # link of 'b' with previous object is broken now as new object is
    return a,b
a = 10
b = 20
print('a:{} , b:{}'.format(a,b))
swap(a,b)
print('swap(10,20):', swap(10,20))
print('a:{} , b:{} after swap'.format(a,b))

## cant change global scope

print('-----------------------------')

print('****recursive function****')
# recursive : use same function in the function.
# condition: it has to be a condition to end a loop.
# LIMITS: 1- just 1 parameter allows.  2-memory limits.
# at all it does not recommended. too slow. ----------------> use generators instead of recursive.

print('factoriel')
def factoriel (n):
    if n <2:
        return 1
    else:
        return n * factoriel(n-1)
print(factoriel(5))

def sumof (n):
    if n == 0:
        return 0
    else:
        return n + sumof(n-1)
print(sumof(5))

def fibo (n):
    if n == 0:
        return 0
    elif n<3:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
for i in range (10):
    print(fibo(i))

print('-----------------------------')


print('*args , **kwargs')
# args & kwargs
# *args
# When we are not sure about the number of arguments being passed to a function then we can use *args as,
# function parameter. *args allow us to pass the variable number of Non Keyword Arguments to function.
# We can simply use an asterisk * before the parameter name to pass variable length arguments.
# The arguments are always passed as a tuple.
# We can rename it to anything as long as it is preceded by a single asterisk (*).
#  It's best practice to keep naming it args to make it immediately recognizable.

# **kwargs
# **kwargs allows us to pass the variable number of Keyword Arguments to the function.
# We can simply use an double asterisk ** before the parameter name to pass variable length arguments.
# The arguments are passed as a dictionary.
# We can rename it to anything as long as it is preceded by a double asterisk (**).
# It's best practice to keep naming it kwargs to make it immediately recognizable.

def add(a, b, c):
    return a + b + c
print(add(10, 20, 30))  # Sum of two numbers

# print(add(1,2,3,4)) '''This will throw below error as this function will only take 3 argument
# If we want to make argument list and tuple dynamic then *args wil come in picture'''
def add1(*args):
    return sum(args)
print(add1(1,2,3))
print(add1(1,2,3,4)) # *args will take dynamic argument list and tuple. So add() function w
print(add1(1,2,3,4,5))
print('\n')
list1=[1,2,3,4,5]
tuple1=(1,2,3,4,5)
print(add1(*list1))
print(add1(*tuple1))
print(add1(1,2,*list1))

def UserDetails(**kwargs):
    print(kwargs)
UserDetails(Name='Asif' , ID=7412 , Pincode=41102 , Age= 33 , Country= 'India')

def UserDetails(**kwargs):
    for key,val in kwargs.items():
        print("{} :- {}".format(key,val))

mydict = {'Name': 'Asif', 'ID': 7412, 'Pincode': 41102, 'Age': 33, 'Country': 'India'}
UserDetails(**mydict)
print('=========')
def UserDetails(licenseNo, *args , phoneNo=0 , **kwargs): # Using all four argum
    print('License No :- ', licenseNo)
    for i in args:
        print('Full Name :-',i)
    print('Phone Number:- ',phoneNo)
    for key,val in kwargs.items():
        print("{} :- {}".format(key,val))
mylist=['ali','reza']
mydict = {'Name': 'Asif', 'ID': 7412, 'Pincode': 41102, 'Age': 33, 'Country': 'India'}

UserDetails(92354,*mylist,**mydict)


# **** __name__:

# assume we have module with some functions in it.( functions print something).
# then, when we import the module in a file, unintentionally the print methods of module , will run that is undesirable.
# solution: use __name__ in module body .

#def ......
# ...
# ...
# ...
# def ....
# ...
# if __name__ == '__main':
#     print(.......)


# **** docstring:
# use for write help for functions.------->  """ ********** """
# how to access: help(name of function)

# nested function:
# when we have a function in the function.
def outer():
    a= 0
    def inner():
        nonlocal a #-------> a is not global, also is not local for inner():
        # a :  is nonlocal or enclosing for inner().
        pass
        inner()  # call inner function inside of outer function.

    # order of checking variable:
    # 1- local 2- enclosing 3- global 4- builtin


















