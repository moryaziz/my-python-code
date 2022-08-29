# Description:
#
#         Write a Python program that prints the number of days in a given month.
#
#         The value of the variable month is the name of the month with the first letter capitalized.
#
#         Do not consider leap years for the number of days in February.
#
#         You can add a customized message. For example: "<month> has: <num_days> days."

month_list ={'jan':31,'feb':28,'mar':31}
def month():
    num = input('please enter a month')
    if num in month_list:
        print('{}={}days'.format(num,month_list[num]))
month()





