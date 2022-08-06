
#List

# 1) List is an ordered sequence of items.
# 2) We can have different data types under a list.
    # E.g we can have integer, float and string items in a same list. but it isn't recommended.


# List Creation
list1=[]
list2 = ['Asif', 25 ,[50, 100],[150, 90] , {'John' , 'David'}]
print('list2:', list2)
print(list2[0]) # Retreive first element of the list
print(list2[-1]) # Last item of the list
list2 = [1 , 2 , 3] # list member can be updated and changed
print('list2:', list2)
print('------------------')

# List method:
string = 'abcd'
list1 = [string]
print(list1) #---->['abcd']
list2 = list(string) # list method get iterable object and each element will be member of list.
print(list2) #----->['a', 'b', 'c', 'd']


print('------------------')


# List Slicing
list3 = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
# [start:stop:step]
print(list3[1:6:2])

print('------------------')

#**** mutable and immutable: *****

# list is mutable object.
# mutable object: after set and get id, it cannot be changed
# and if changes, for saving , we have to pass it to different location(id).
# we have to consider mutable, in some cases they are much faster.
a = 5
b = a
print('id(a)):',hex(id(a)))
print('id(b)):',hex(id(b)))
# address of a and b are equal and point to same address(5).
a = a + 23
print('b:',b)
print('id(a)):',hex(id(a)))
print('id(b)):',hex(id(b)))
# amount and address of b , is not changed. but id of 'a' is changed, because numeric is immutable.
print('------------------')
a = [5,6]
b = a # b pointed to 'a'.
print(hex(id(a)))
print('id(b)):',hex(id(b)))
a.append(7)
print(a)
print('b:',b) # as 'a' is a list and changes in its constant address, then b is changed because 'a' is changed.
print('id(a)):',hex(id(a))) # list is mutable. so id of 'a' stay constant.

print('------------------')
print('\n')

# Add , Remove & Change Items on List
list3.append('nine') # Add an item to the end of the list
list3.insert(9,'ten') # Add item at index location 9
print(list3)
list3.insert(1,'NEW ONE') # Add item at index location 1
print(list3)
list3.remove('NEW ONE') # Remove item "ONE"
list3.pop(8) # Remove item at index location 8
print(list3)
del list3[7] # Remove item at index location 7
list3.clear() # Empty List / Delete all items in the list
print(list3)
del list3 # Delete the whole list


## Copy List
list4 = ['one' , 'two' , 'three' , 'four']
mylist4 = list4 # The address of both list4 & mylist4 will be the same
list4.pop(3) # any change on list, will be saved on mylist4.
print(list4)
print(mylist4)
mylistcopy = list4.copy() # Create a copy of the list
list4.pop(2)
print(mylistcopy) # The address of mylistcopy will be different from list4
print(id(list4) == id(mylistcopy)) #---false

print('-------------------------')

# Join Lists
list1 = ['one', 'two', 'three', 'four']
list2 = ['five', 'six', 'seven', 'eight']
list3 = list1 + list2 # Join two lists by '+' operator
print('list3:' , list3)
list1.extend(list2) #Append list2 with list1
list3 = list1 + list2 # Join two lists by '+' operator
print('list1:' , list1)
print('list3 = list1.extend(list2) + list2:' , list3)


# check List Membership
list1 = ['one', 'two', 'three', 'four']
print('one' in list1) #---ture
print('on' in list1)  #---false---list check the exact word

print('-------------------------')

# Loop through a list
list1 = ['one', 'two', 'three', 'four' , 'one']
print('loop:')
for i in list1:
    print(i)
for i in enumerate(list1):
 print(i)
for i ,j in enumerate(list1):
    print(i,j)

print('-------------------------')

# Count
print('count:', list1.count('one')) # Number of times item "one" occurred in the list.


# List Comprehensions : List Comprehensions provide an elegant way to create new lists.
mystring = "WELCOME"
mylist = [ i for i in mystring ] # Iterating through a string Using List Comprehensions
print(mylist)
# these tow method for List Comprehensions have same results.
mylist1 = []
for i in mystring:
    mylist1.append(i)
print(mylist)
mylist2 = [ i for i in range(40) if i % 2 == 0]
print(mylist2)









