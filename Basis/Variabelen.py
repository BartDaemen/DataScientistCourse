# creating variables

	# Python has no command for declaring a variable.
	# A variable is created the moment you first assign a value to it.
	# Variables do not need to be declared with any particular type, and can even change type after they have been set.
	# Variable names are case-sensitive.

x = 5
y = "John"
print(x)
print(y)

# type variabelen

	# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y)) 

	# String variables can be declared either by using single or double quotes

# Variabelen namen

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)
    # A variable name cannot be any of the Python keywords.

		# Variabele naam bevat geen spaties
			# Camel-case:  myVariableName = "John" 
			# Pascal-case:  MyVariableName = "John" 
			# Snake-case:  my_variable_name = "John" 

myvar = "John"
my_var = "John"
_my_var = "John"

myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Global variables
	# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
	# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 

# If you create a variable with the same name inside a function, this variable will be local, 
# and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x) 

