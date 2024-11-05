# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# creating a function

def my_function():
  print("Hello from a function") 

# calling a function

def my_function():
  print("Hello from a function")

my_function()

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# Return values

def my_function(x):
  return 5 * x # To let a function return a value, use the return statement:

print(my_function(3))
print(my_function(5))
print(my_function(9))
