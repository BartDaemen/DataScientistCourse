# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# type:  <class 'tuple'> 

# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Since tuples are indexed, they can have items with the same value:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# tuple length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# tuple constructor: It is also possible to use the tuple() constructor to make a tuple.

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Access Tuple Items
  # You can access tuple items by referring to the index number, inside square brackets:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #
Note: The first item has index 0.

# Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 

# Change tuple values

  # Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
  # But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 

# Loop through a tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i]) 
