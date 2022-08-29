#Sets
#1) Unordered & Unindexed collection of items.
#2) Set elements are unique. Duplicate elements are not allowed.
#3) Set elements are immutable (cannot be changed).
#4) Set itself is mutable. We can add or remove items from it.


# Set Creation
myset = set() # Create an empty set
myset = {1,2,3,4,5} # Set of numbers
my_set = {1,1,2,2,3,4,5,5} # Duplicate elements are not allowed and removed.
print(my_set)
myset3 = {10,20, "Hola", (11, 22, 32)} # Mixed datatypes
# myset3 = {10,20, "Hola", [11, 22, 32]} # set doesn't allow mutable items like lis


# Loop through a Set
myset = {'one', 'two', 'three', 'four', 'five'}
for i in myset:
    print(i)


print('----------------------------')
# Set Membership
print('one' in myset) # Check if 'one' exist in the set)


# Add & Remove Items
print('Add & Remove Items')
myset = {'one', 'two', 'three', 'four', 'five'}
myset.add('NINE') # Add item to a set using add() method
print(myset)
myset.update(['TEN' , 'ELEVEN' , 'TWELVE']) # Add multiple item to a set using update() method.
print(myset)
myset.remove('NINE') # remove item in a set using remove() method
myset.discard('TEN') # remove item from a set using discard() method
myset.clear() # Delete all items in a set

print('----------------------------')


# Copy Set
myset = {'one', 'two', 'three', 'four', 'five'}
print( myset)

myset1 = myset  # Create a new reference "myset1"
print(id(myset) , id(myset1)) # The address of both myset & myset1 will be the same as
myset.add('TEN')
print(id(myset) , id(myset1))
    # after updating myset, the address of both still be as same as.
print('my set after update:', myset)
print(myset1)
    # after updating myset, myset1 is also changed.

my_set = myset.copy() # Create a copy of the list and tuple
print(id(myset) , id(my_set))
    # # The address of my_set will be different from myset because my_set is copy.

print('----------------------------')

# Set Operation
    # Union
A = {1,2,3,4,5}
B = {4,5,6,7,8}
C = {8,9,10}
A.union(B) # Union of A and B
D = A.union(B) # Union of A and B
print('A:', A) # A itself did not changed.
print('D:', D)
print('A.union(B):', A.union(B))
A.union(B, C) # Union of A, B and C.
A.update(B,C)
print('A.update(B,C):', A) # A itself changed after update.

    # Intersection : Common items in both sets
A.intersection(B) #Intersection of A and B
print('A.intersection(B):', A) # A itself did not changed.
A.intersection_update(B)
print('A.intersection_update(B):', A)

    #Difference :  set of elements that are only in A but not in B
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print('A:{}, B:{}'.format(A,B))
A.difference(B) # Difference of sets
print('A.difference(B)')
print('A:', A) # A itself did not changed.
print('A.difference(B):', A.difference(B))
B.difference_update(A)
print('B.difference_update(A)',B)

    # Symmetric Difference
A = {1,2,3,4,5}
B = {4,5,6,7,8}
# Symmetric difference (Set of elements in A and B but not in both.
A.symmetric_difference(B) # Symmetric difference of sets
print('A.symmetric_difference(B)')
print('A:', A) # A itself did not changed.
A.symmetric_difference_update(B)
print('A.symmetric_difference_update(B):', A)

print('----------------------------')

#Subset , Superset & Disjoint
A = {1,2,3,4,5,6,7,8,9}
B = {3,4,5,6,7,8}
print(B.issubset(A)) # Set B is said to be the subset of set A if all elements of B are in A.
print(A.issuperset(B)) # Set A is said to be the superset of set B if all elements of B are in A.
print(B.isdisjoint(A)) # Two sets are said to be disjoint sets if they have no common ellements.

#Other Builtin functions
    #sum , max , min , len
    #enumurate , sorted(A,reverse=True)

















