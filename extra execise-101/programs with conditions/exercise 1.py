# Description:
#
#         Write a Python program that prints if a number num is either "Positive", "Negative", or "Zero".

def check_sign(num):
    if num == 0:
        print('zero')
    elif num >0:
        print('positive')
    else:
        print('negative')

check_sign(5)

check_sign(-5)


