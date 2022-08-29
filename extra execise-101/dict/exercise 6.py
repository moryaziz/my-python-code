# Description:
#
#         Write a Python program that prints the smallest value in a dictionary.
#
#         If the dictionary is empty, print None.
#
#         You may assume that the values are numeric.

my_dict1 = {"a": 1, "b": 1, "c": 3}
my_dict2 = {}
list1 = list(my_dict1.values())
if not len(my_dict1) == 0:
    print(min(my_dict1.values()))
else:
    print('none')



