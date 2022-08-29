# Description:
#         Write a Python program that prints a list with the elements that listA and listB have in common.
#         If they don't have any elements in common, print an empty list.
#         The program should not assume that the lists have the same length.
#         You may assume that each element will only appear once in each list.

listC = []
def common(listA,listB):
    global listC
    listC.clear()
    for i in listA:
        if i in listB:
            listC.append(i)
        else:
            continue

common([1,2,3,4],[1,2])
print(listC)
common([1,2,3,4],[1,2,3])
print(listC)
common([],[1,2,3,4])
print(listC)






