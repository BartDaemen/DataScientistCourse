
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets
# List items are ordered, changeable, and allow duplicate values.
    # When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
    # If you add new items to a list, the new items will be placed at the end of the list.
# A list can contain different data types:
# list type: <class 'list'>


# List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List length

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # Print the number of items in the list:

# List constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Access list items

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # List items are indexed and you can access them by referring to the index number / start index is 0

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # last item

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # The search will start at index 2 (included) and end at index 5 (not included).

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Change list item

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Add list items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # append adds at end of list
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") # The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # To append elements from another list to the current list, use the extend() method.

# Remove list items

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # The remove() method removes the specified item. / If there are more than one item with the specified value, the remove() method removes the first occurrence:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) The pop() # method removes the specified index.

thislist = ["apple", "banana", "cherry"]
del thislist[0] #The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.clear() # The clear() method empties the list.

# Loop through lists

  # You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): # Print all items by referring to their index number:

# sort lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() # List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) # To sort descending, use the keyword argument reverse = True:

# join two lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
print(thislist)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

