#A set is a collection which is unordered, unchangeable(can add and remove), and unindexed.
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Unordered means that the items in a set do not have a defined order.
#Sets cannot have two items with the same value.

#To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#To add items from another set into the current set, use the update() method.
"""
The object in the update() method does not have to be a set,
it can be any iterable object (tuples, lists, dictionaries etc.).
"""
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Remove "banana" by using the remove() method:
#Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Remove "banana" by using the discard() method:
#Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#pop() removes random item from set.
#The clear() method empties the set:

#union: Returns a new set with the union of elements. Does not modify the original set.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#update: Modifies the original set by adding elements from another set. Returns None.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Use | to join set with sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
"""
Note: The  | operator only allows you to join sets with sets,
and not with other data types like you can with the  union() method.
"""

"""
The intersection() method will return a new set,
 that only contains the items that are present in both sets.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#or you can just use & sign instead of intersection (but both must be sets)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

"""
The intersection_update() method will also keep ONLY the duplicates,
 but it will change the original set instead of returning a new set.
"""

"""
The difference() method will return a new set that will contain only
 the items from the first set that are not present in the other set.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
#you can use - sign instead of difference, but you can only join sets with sets

"""
The difference_update() method will also keep the items from the first set
that are not in the other set, but it will change the original set instead of returning a new set.
"""

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.



