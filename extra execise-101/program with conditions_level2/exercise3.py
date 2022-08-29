# Description:
#
#         Write a Python program that simulates an interactive calculator with the basic arithmetic operations in Python (addition, subtraction, multiplication, division, integer division, and modulo).
#
#         The program must interact with the user by asking for the values and the type of operation that will be performed.
# The output should include the values, the operation, and the result (as shown below).
# The type of operation will be denoted by an integer.
# - 1 for addition
# - 2 for subtraction
# - 3 for multiplication
#  4 for division
# - 5 for integer division
#  - 6 for modulo
# the program should present an initial message to the user describing the types of operations and the integer that has to be entered to select each one of them.
#  If the values entered by the user are invalid for the operation selected, a descriptive message should be displayed. For example, for a division operation the denominator cannot be 0.
# If the user enters an invalid integer to select the operation, print
# "Please choose a valid operation"

def calculate():
    print ('=== Welcome to your Interactive Python Calculator ===')
    first_value = int(input('Please enter the first value:'))
    second_value = int(input('Please enter the second value:'))
    print ('Great! Now enter the operation.')
    print('These are the available options:')
    print('1 - Addition\n','2 - Subtraction\n',
          '3 - Multiplication\n','4 - Division\n',
          '5 - Integer Division\n','6 - Modulo')
    operator = int(input('Enter the corresponding integer:'))
    def add(x,y):
        return (x + y)
    def sub(x,y):
        return x - y
    def multi(x,y):
        return x * y
    def divi(x,y):
        return x / y
    def integer_divi(x,y):
        return x // y
    def modu(x,y):
        return x % y
    if operator == 1:
        print(add(first_value,second_value))
    if operator == 2:
        print(sub(first_value,second_value))
    if operator == 3:
        print(multi(first_value,second_value))
    if operator == 4:
        print(divi(first_value,second_value))
    if operator == 5:
        print(integer_divi(first_value,second_value))
    if operator == 6:
        print(modu(first_value,second_value))

calculate()