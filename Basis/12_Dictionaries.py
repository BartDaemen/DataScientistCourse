# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
# Type:  <class 'dict'> 

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Dictionaries cannot have two items with the same key:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionary length

print(len(thisdict)) 

# Dict constructor

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Access items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# Get keys
# The keys() method will return a list of all the keys in the dictionary.

 x = thisdict.keys() 

# Get values
# The values() method will return a list of all the values in the dictionary.

 x = thisdict.values() 

# Get items
# The items() method will return each item in a dictionary, as tuples in a list.

 x = thisdict.items() 

# change values
# You can change the value of a specific item by referring to its key name:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# add items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# remove item

# The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")

#The del keyword removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]

# The clear() method empties the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()

# loop through a dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)
  

# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x]) 

#You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x) 

#You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)

Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y) 

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

#returns
"""brand Ford
model Mustang
year 1964"""

# nested dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

  # access items in nested dict

  print(myfamily["child2"]["name"]) 

# loop through nested dict

  for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])
  

