# Description:
#         Write a Python program that prints the second largest value in a list.
#         If the list is empty or only has one element, print None.

listC = []
def second_max(list):
    if len(list)>1:
        list.remove(max(list))
        print(max(list))
    else:
        print('none')

second_max([1,5,10])




