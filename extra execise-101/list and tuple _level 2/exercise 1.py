# Description:
#
#         Write a Python program that prints (as a list) the elements of listA that are not in listB as a list.
#         If the lists have the same elements, print an empty list.
#         If listA is an empty list, print an empty list.

def differece(listA,listB):
    setA = set(listA)
    setB = set(listB)
    setA.difference_update(setB)
    mylistA = list(setA)
    print(mylistA)

differece([1,2,3,4],[1,2])
differece([1,2,3,4],[1,2,3])
differece([],[1,2,3,4])

print('-------------------------')

listC = []
def differece2(listA,listB):
    global listC
    listC.clear()
    for i in listA:
        if not i in listB:
            listC.append(i)
        else:
            continue

            
differece2([1,2,3,4],[1,2])
print(listC)
differece2([1,2,3,4],[1,2,3])
print(listC)
differece2([],[1,2,3,4])
print(listC)

# for i in mylistB:
#     mylistA.pop(i)
# print(mylistA)
# print(setA)




