# Description:
#
#         Write a Python program that counts the number of elements in a list with value greater than 3.
#         You may assume that the list only contains numbers.
#         Print the final count.

def greater_elements(list):
    # if len(list) == 0:
    #     print ('empty list')
    # else:
    count = 0
    for i in list:
        if i > 3 :
            count +=1
    print (count)

list = []
list1 = [1,4,2,2,2,2,2,3,3,4]
greater_elements(list)
greater_elements(list1)






