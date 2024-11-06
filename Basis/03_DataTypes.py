# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:
  # Text Type: 	      str
  # Numeric Types: 	  int, float
  # Sequence Types: 	list, tuple, range
  # Set Types: 	      set
  # Boolean Type: 	  bool
  # None Type: 	      NoneType

# getting the data type

x = 5
print(type(x))

# setting the data type

  # x = "Hello World" 	                str 	
  # x = 20 	                            int 	
  # x = 20.5                           	float 	
  # x = ["apple", "banana", "cherry"] 	list 	
  # x = ("apple", "banana", "cherry") 	tuple 	
  # x = range(6) 	                      range 	
  # x = {"name" : "John", "age" : 36} 	dict 	
  # x = {"apple", "banana", "cherry"} 	set 	
  # x = True 	bool 	
  # x = None 	NoneType

# Setting the Specific Data Type
  
  # x = str("Hello World") 	str 	
  # x = int(20) 	int 	
  # x = float(20.5) 	float 	
  # x = list(("apple", "banana", "cherry")) 	list 	#let op de ronde haakjes
  # x = tuple(("apple", "banana", "cherry")) 	tuple 	# let op de ronde haakjes
  # x = range(6) 	range 	
  # x = dict(name="John", age=36) 	dict 	
  # x = set(("apple", "banana", "cherry")) 	set 	

# type conversion

# You can convert from one type to another with the int(), float(), str()

x = 1    # int
y = 2.8  # float
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)

# strings

  # Strings in python are surrounded by either single quotation marks, or double quotation marks.
  # 'hello' is the same as "hello".
  # You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
  # You can display a string literal with the print() function:

print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# strings are arrays

  # Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1]) # returns e

  # Looping through a string

for x in "banana":
  print(x)

  # string length

a = "Hello, World!"
print(len(a))

# check string:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
if "free" not in txt:
  print("Yes, 'free' is not present.")

# string slicing

  # You can return a range of characters by using the slice syntax.
  # Specify the start index and the end index, separated by a colon, to return a part of the string.


b = "Hello, World!"
print(b[2:5]) # Get the characters from position 2 to position 5 (not included)

b = "Hello, World!"
print(b[:5]) # Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[2:]) # Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[-5:-2]) # Use negative indexes to start the slice from the end of the string:

# modify strings

  # The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

  # The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

  # The strip() method removes any whitespace from the beginning or the end:

print(a.strip()) # returns "Hello, World!"

  # The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

# string concatenation
  # To concatenate, or combine, two strings you can use the + operator.

a = "Hello"
b = "World"
c = a + b
print(c) #returns HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c) #returns Hello World

# format strings / f-strings
  # To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
  # A placeholder can contain variables, operations, functions, and modifiers to format the value.

age = 36
txt = f"My name is John, I am {age}"
print(txt)

A placeholder can include a modifier to format the value.

  # A placeholder can include a modifier to format the value.

price = 59
txt = f"The price is {price:.2f} dollars" #fixed point with 2 decimals
print(txt)


# escape characters

  # \'	Single Quote	
  # \\	Backslash	
  # \n	New Line	
  # \t	Tab	
  # \b	Backspace	



  
