# Description:
#
#         Write a Python program that determines if three numbers (a, b, and c) are in increasing order, decreasing order, or none.
#
#         If a > b > c, print "Decreasing Order".
#
#         If a < b < c, print "Increasing Order".
#
#         Else, print "None".

def order(*args):
    MY_LIST=[j for j in args]
    length = len(MY_LIST)
    result = ''
    for i in range(length-1):
        # print(i)
        # for j in (args):
        #     print(j)
        if MY_LIST[i] == MY_LIST[i+1]:
            result = 'none'
            break
        elif MY_LIST[i]<MY_LIST[i+1]:
            result = 'increasing order '
        elif MY_LIST[i] > MY_LIST[i+1]:
            result = 'decreasing order'
        # else:
        #     result = 'NONE'

            #     break
            # else:
            #     result = 'equal'
            # # print(result)
    print(result)

order(1,1,1,2)
order(2,1,1)
order(2,1)
order(1,2,3)





