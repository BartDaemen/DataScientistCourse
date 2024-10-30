# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:
  # Text Type: 	str
  # Numeric Types: 	int, float
  # Sequence Types: 	list, tuple, range
  # Set Types: 	set
  # Boolean Type: 	bool
  # None Type: 	NoneType

# getting the data type

x = 5
print(type(x))

# setting the data type

  # x = "Hello World" 	  str 	
  # x = 20 	              int 	
  # x = 20.5             	float 	
  # x = ["apple", "banana", "cherry"] 	list 	
  # x = ("apple", "banana", "cherry") 	tuple 	
  # x = range(6) 	range 	
  # x = {"name" : "John", "age" : 36} 	dict 	
  # x = {"apple", "banana", "cherry"} 	set 	
  # x = True 	bool 	
  # x = None 	NoneType

# Setting the Specific Data Type
  
  # x = str("Hello World") 	str 	
  # x = int(20) 	int 	
  # x = float(20.5) 	float 	
  # x = list(("apple", "banana", "cherry")) 	list 	
  # x = tuple(("apple", "banana", "cherry")) 	tuple 	
  # x = range(6) 	range 	
  # x = dict(name="John", age=36) 	dict 	
  # x = set(("apple", "banana", "cherry")) 	set 	

# type conversion

# You can convert from one type to another with the int(), float()

x = 1    # int
y = 2.8  # float
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)

