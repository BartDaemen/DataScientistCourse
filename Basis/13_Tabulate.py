# Use the tabulate library in Python to create well-formatted tables. 

#### Voorbeeld 1

# Import the tabulate module
from tabulate import tabulate

# Sample data: list of lists
data = [
    ["Alice", 24, "Engineer"],
    ["Bob", 30, "Data Scientist"],
    ["Charlie", 28, "Teacher"]
]

# Creating a table with headers and a grid format
table = tabulate(
    data, 
    headers=["Name", "Age", "Profession"], 
    tablefmt="grid"
)

print(table)

### Voorbeeld 2

# Sample sales data
sales_data = [
    ["Q1", 15000, 12000, 13000],
    ["Q2", 17000, 16000, 14500],
    ["Q3", 18000, 15000, 16000],
    ["Q4", 20000, 21000, 19000]
]

headers = ["Quarter", "Product A", "Product B", "Product C"]

# Import tabulate library
from tabulate import tabulate

# Displaying sales data using the 'fancy_grid' format
table_fancy = tabulate(sales_data, headers=headers, tablefmt="fancy_grid")

print(table_fancy)
