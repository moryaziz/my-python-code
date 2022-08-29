# Description:
#
# Write a Python program that prints the largest and smallest values in a list
# Print the two values on the same line, separated by a space.
# The largest value should appear first and the smallest value should appear second.
# You may assume that the list only contains numeric values.
# If the list is empty, print None.

def max_of_list(list):
    if list == []:
        print ([])
    else:
        print(max(list), min(list))
mylist = [1,2,3,4]
mylist1 = [-1,-2,-3,-4]
mylist2 = []

max_of_list(mylist)
max_of_list(mylist1)
max_of_list(mylist2)

# print(max(mylist),min(mylist))
# print(max(mylist1),min(mylist1))
# print(max(mylist2))