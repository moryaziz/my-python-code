# Description:
#
#         Write a Python program that prints the digits of a number in reverse order on the same line.
#
#         If the number only has one digit, print this digit.

def reverse(n):
    length = 0
    for i in range(1,n):
        if n // (10**i) < 10:
            # print(10**i)
            break
    length = i+1
    # print(length)
    new_num = 0
    if n<10:
        new_num = n
    else:
        for i in range (i,-1,-1):
            new_num += n % 10 * 10**i
            n = n//10
        # print(n)
    print(new_num)
reverse(123)

# print(125//10)
# print(/12%10)






