# Python has two primitive loop commands:

#     while loops
#     for loops


# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i)
  i += 1

# With the break statement we can stop the loop even if the while condition is true:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

# With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x) # print elke letter afzonderlijk

# With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#  To loop through a set of code a specified number of times, we can use the range() function,

for x in range(6):
  print(x) # 

Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

for x in range(6):
  print(x)
else:
  print("Finally finished!") 

# nested loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 


