# Description:
#         Write a Python program that checks if a list is empty or not.
#         If the list is empty, print "Empty". Else, print "Not Empty".

def max_of_list(list):
    if len(list) == 0:
        print ('empty')
    else:
        print('not empty')

list = []
list1 = [4]
max_of_list(list)
max_of_list(list1)