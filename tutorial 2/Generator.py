# Generator
# Python generators are easy way of creating iterators.
# It generates values one at a time from a 'given sequence' instead of returning the entire sequence at once.
# It is a special type of function which returns an iterator object.
# In a generator function, a 'yield' statement is used rather than a 'return' statement.
# Generator cannot include the return keyword. If we include it then it will terminate the execution of the function.
# The difference between yield and return is that :
# once yield returns a value the function is paused and the control is transferred to the caller.
# Local variables and their states are remembered between successive calls. (it save where you were before yield.)
# In case of the return statement value is returned and the execution of the function is terminated.
# Methods like iter() and next() are implemented automatically in generator function.
# Simple generators can be easily created using generator expressions.
# Generator expressions create anonymous generator functions like lambda.
# The syntax for generator expression is similar to that of a list and tuple comprehension but the only
# difference is square brackets are replaced with round parentheses.
# Also list and tuple comprehension [] produces the entire list and tuple while the generator expression () produces:
# one item at a time which is more memory efficient than list and tuple comprehension.

# Simple generator function that will generate natural numbers from 1 to 20.
# before we write like this: we use return and save values in a list and tuple
def mygen():
    a = list()
    for i in range(1, 20):
        #print(i)  # WE CANT use return in THE FOR, because the loop will break.
        a.append(i)
    return a


my_gen = mygen()
print('a as list and tuple by return=', my_gen)

# but when we use yield, we can achieve any value without breaking the loop.
def mygen1():
    for i in range(1, 10):
        yield i

a = list()
for i in mygen1():
    a.append(i)
print('a as list and tuple by yield=', a)

# list and tuple and generator comprehension:

list1 = [i for i in fibo()] # List comprehension
# this writting method is like get return as list and tuple.
print(list1)

gen1 = (i for i in fibo()) # generator comprehension
# this writting method is like get yield.
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# khodam: when use yield: you have to use for to achive all iterable values.
for num in gen1:
    print(num)




def fibo():
    pervious = 0
    now = 1
    count = 1
    while count<10:
        yield (pervious + now)
        # when we iterate fibo, after this sentence,function be paused and continue from here after calling again.
        count +=1
        pervious,now = now,pervious + now


for i in fibo():
    print(i)







