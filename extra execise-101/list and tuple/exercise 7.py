# Description:
#
# Write a Python program that removes duplicate elements from a list,
# only keeping one occurrence of each element in the list.
# The original list should be mutated (modified).
# The program must print the final version of the list.

def remove_elements(list):
    if len(list) == 0:
        print ('empty list')
    else:
        for i in list:
            for j in range(list.count(i)-1):
                list.remove(i)
        print(list)

list = []
list1 = [1,2,2,2,2,2,3,3,4]
list2 = ['a','a','b','c','b']
remove_elements(list)
remove_elements(list1)
remove_elements(list2)



