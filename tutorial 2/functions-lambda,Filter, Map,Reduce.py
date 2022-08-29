# Lambda, Filter, Map and Reduce

# Lambda
# A lambda function is an anonymous function (function without a name).
# Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned.
# We use lambda functions when we require a nameless function for a short period of time.

    ## syntax : lambda argument(s) : expression
    ## lambda num1,num2 : num1 + num2

# Filter
# It is used to filter the iterables/sequence as per the conditions.
# Filter function filters the original iterable and passes the items
        #  that returns True for the function provided to filter.
# It is normally used with Lambda functions to filter list and tuple, tuple, or sets.
# filter() method takes two parameters:
    # function - function tests if elements of an iterable returns true or false
    # iterable - Sequence which needs to be filtered, could be sets, lists, tuples, or any iterators

    ## syntax : filter ( function , iterable)
    ## filter (lambda n:n%2 ==1 , list1)

# Map
# The map() function applies a given function to each item of an iterable (list and tuple, tuple etc.)
        # and returns a list and tuple of the results.
# map() function takes two Parameters :
    # function : The function to execute for each item of given iterable.
    # iterable : It is a iterable which is to be mapped.
# Returns : Returns a list and tuple of the results after applying the given function
        # to each item of a given iterable (list and tuple, tuple etc.)

        ## syntax : map ( function , iterable)
        ## map (lambda num : num*2 , list1)

# Reduce
# The reduce() function is defined in the functools python module.
# The reduce() function receives two arguments, a function and an iterable.
# However, it doesn't return another iterable, instead it returns a single value.
# Working:
# 1) Apply a function to the first two items in an iterable and generate a partial result.
# 2) The function is then called again with the result obtained in step 1 and the next value in the
# sequence. This process keeps on repeating until there are items in the sequence.
# 3) The final returned result is returned and printed on console.

        ## syntax : reduce ( function , iterable)
        ## reduce (lambda a,b : a+b , list1)

###lambda
print('lambda')
addition = lambda a : a + 10 # This lambda function adds value 10 to an argument
print(addition(5))

res = (lambda *args: sum((args))) # This lambda function can take any number of argrs
print(res(10,20)) , res(10,20,30,40)

res1 = (lambda **kwargs: sum(kwargs.values())) # This lambda function can take an **kwargs
print(res1(a = 10 , b= 20 , c = 30))


### filter
print('filter')
list1 = [1,2,3,4,5,6,7,8,9]
# The below Filter function filters "list1" and passes all odd numbers using lamb
odd_num = list(filter(lambda n: n%2 ==1 ,list1))
print(odd_num)

### map
print('map')
def twice(n):
    return n * 2
doubles = list(map(twice, odd_num))  # The map function will apply user defined "tw
print(doubles)

### reduce
print('reduce')
from functools import reduce
def add(a, b):
    return a + b
sum_all = reduce(add, doubles)  # This reduce function will perform sum of all item
print(sum_all)

#The below reduce() function will perform sum of all items in the list and tuple using lambda
sum_all = reduce(lambda a,b : a+b,doubles)
print(sum_all)



















