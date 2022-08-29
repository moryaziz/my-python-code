# Description:
#
#         Write a Python program that prints the second smallest value in a list.
#         If the list is empty or only has one element, print None.

listC = []
def second_min(list):
    if len(list)>1:
        list.remove(min(list))
        print(min(list))
    else:
        print('none')

second_min([1])
