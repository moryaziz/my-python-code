# Description:
# Write a Python program that creates and print a dictionary that maps each element in a list
# to its corresponding frequency (how many times it occurs in the list).
# The test should be case-sensitive. Therefore, "A" should not be considered the same element as "a".

def cal_frequency(list):
    dict ={}
    count = 0
    for i in set(list):
        for j in list:
            if i == j:
                count += 1
            else:
                continue
        dict[i] = count
        count = 0
    return dict
print(cal_frequency([1,1,2,3,4,4,4,1,2]))
print(cal_frequency(['a','a']))








