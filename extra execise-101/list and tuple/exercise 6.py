# Description:
#
#         Write a Python program that removes all occurrences of the element elem_to_remove from a list.
#         The output of the program should be the new list with the element removed.
#         If the element is not found in the list, print the message "Not Found".
#         If the list is empty, print "Empty List".

list = [1,2,2]
list.remove(2)
print(list)
print(list.count(2))
def remove_elements(list,elem):
    if len(list) == 0:
        print ('empty list')
    else:
        for i in range(list.count(elem)):
            list.remove(elem)
        print(list)

list = []
list1 = [1,2,2,2,2,2,3,3,4]
remove_elements(list,2)
remove_elements(list1,2)





