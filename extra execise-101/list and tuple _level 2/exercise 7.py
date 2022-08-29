# Description:
#
#         Write a Python program that prints a "flattened" version of a list that contains nested lists.
#         "Flattened" means that all the elements in the nested lists should be added to a main list such that
#         it doesn't contain any nested lists, just the individual.
#         The list could contain other elements that are not lists or other sequences,
#         so you must check the type of each element and act appropriately.
#         If the list is empty, print an empty list.

list1 = [1,[1,2,3],[4,5,6],(7,8),'a']
list2 = []
for i in list1:
    if isinstance(i,list):
        for j in i:
            if isinstance(j, int):
                list2.append(j)
    if isinstance(i,tuple):
        for j in i:
            if isinstance(j, int):
                list2.append(j)
    if isinstance(i,set):
        for j in i:
            if isinstance(j, int):
                list2.append(j)
    else:
        if isinstance(i, int):
            list2.append(i)
        elif isinstance(i, str):
            list2.append(i)


print(list2)


