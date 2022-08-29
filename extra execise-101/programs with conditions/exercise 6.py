# Description:
#
#         Write a Python program that prints "Equal" if three numbers a, b, and c are equal.
#
#         If at least one number if different, the program should print "Not Equal".

def equallity(*args):
    result = ''
    for i in (args):
        # print(i)
        for j in (args):
            # print(j)
            if i != j:
                result = 'not equal'
                break
            else:
                result = 'equal'
            # print(result)
    print(result)

equallity(1,1,1,1)
equallity(1,1,1,2)






