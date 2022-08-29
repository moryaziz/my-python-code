# Description:
#
#         Write a Python program that prints a triangular pattern like the ones shown below in the examples.
#
#         Each row must have its corresponding number of asterisks. The first row contains one asterisk. The second row contains two asterisks. The third row contains three asterisks and so on.
#
#         The number of rows should be determined by the value of n, a value entered by the user.

def pattern(n):
    for i in range(1,n+1):
        print('* '* i)
pattern(5)



