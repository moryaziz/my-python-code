# Tuples
# 1. Tuple is similar to List except that the objects in tuple are immutable which means
# we cannot change the elements of a tuple once assigned.
# 2. When we do not want to change the data over time, tuple is a preferred data type.
# 3. Iterating over the elements of a tuple is faster compared to iterating over a list.
tup1 = (1, 2, 3)
list1 = [1, 2, 3]
a = tup1
b = list1
print('id(a): {},id(tup1):{}'.format(id(a), id(tup1)))
print('id(b): {},id(list1):{}'.format(id(b), id(list1)))
tup1 = (4, 5)
list1.append(4)
print('after append')
print('id(a): {},id(tup1):{}'.format(id(a), id(tup1)))
print('id(b): {},id(list1):{}'.format(id(b), id(list1)))
print('tup1:', tup1)
print('list1:', list1)
print('a:', a)
print('b:', b)
# list in mutable. after updating list, b is also updated.
# the id of list and b are same and remain unchanged.
# but tuple is immutable. after updating tup1, 'a' is not updated.
# also the id of 'tup1' has changed however the id of 'a' remain unchanged.

print('-----------------------------------')
# Tuple Creation
tup1 = () # Empty tuple
tup5 = ('Asif', 25 ,(50, 100),(150, 90)) # Nested tuples

# Tuple Indexing
print(tup5[0]) # Retreive first element of the tuple
print(tup5[-1]) # Last item of the tuple)

# Tuple Slicing
mytuple = ('one' , 'two' , 'three' , 'four' , 'five' )
print(mytuple[0:3]) # Return all items from 0th to 3rd index location excluding the item)

# Remove & Change Items
# del mytuple[0]
# Tuples are immutable which means we can't DELETE tuple items
# Tuples are immutable which means we can't CHANGE tuple items
del mytuple # Deleting entire tuple object is possible

# Loop through a tuple
mytuple = ('one' , 'two' , 'three' , 'four' , 'five' )
for i in mytuple:
    print(i)

# Count
print(mytuple.count('one')) # Number of times item "one" occurred in the tuple.


print('-----------------------------------')

# Tuple Membership
print('one' in mytuple) # Check if 'one' exist in the list
print('on' in mytuple) # Check if 'one' exist in the list

# Sorting
mytuple2 = (1,2,4,3)
sorted(mytuple2)
print('mytuple2:', mytuple2) #immutable so did not change.
sortedtuple=sorted(mytuple2)
print('sortedmytuple2:',sortedtuple)












