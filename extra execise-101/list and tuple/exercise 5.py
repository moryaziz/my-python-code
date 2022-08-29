# Description:
#
#         Write a Python program that prints the elements of a list followed their corresponding indices.
#         Each element and its index must be on the same line separated by a space.
#         If the list is empty, print "Empty List".


# def index_of_list(list):
#     count = 0
#     if len(list) == 0:
#         print ('empty')
#     else:
#         for i in list:
#             print(i,'',count)
#             count += 1

def index_of_list(list):
    count = 0
    if len(list) == 0:
        print ('empty')
    else:
        for i,j in enumerate(list):
            print(j,i)

list = []
list1 = [1,2,3,4]
index_of_list(list)
index_of_list(list1)