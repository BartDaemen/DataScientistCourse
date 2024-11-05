# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Note: Set items are unchangeable, but you can remove items and add new items.
# Type:  <class 'set'> 

# Set items are unordered, unchangeable, and do not allow duplicate values.
# Unordered means that the items in a set do not have a defined order. / Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Sets cannot have two items with the same value.
  
thisset = {"apple", "banana", "cherry"}
print(thisset) 


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

# Set constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

# Access set items

# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) 

# Add set items

# To add one item to a set use the add() method.

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) 

# To add items from another set into the current set, use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) 

# remove item

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) 

# join sets

# There are several ways to join two or more sets in Python.
  # The union() and update() methods joins all items from both sets.
  # The intersection() method keeps ONLY the duplicates.
  # The difference() method keeps the items from the first set that are not in the other set(s).
  # The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3) 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3) 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3) 
