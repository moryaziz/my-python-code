# Description:
#
# Write a Python program that calculates the factorial of a given number n.
# The value of n should be entered by the user.
# The program must print the result and use a loop to calculate it.
# The factorial of a number n is denoted as n! and it is the result of multiplying all the positive integers that are less than or equal to n.
# For example, 3! = 3 * 2 * 1.
#
# 0! is equal to 1.

def factorial(n):
    fact = 1
    if n == 0:
        fact = 1
    else:
        for i in range(1,n+1):
            fact = fact * i
    print(fact)

factorial(5)






