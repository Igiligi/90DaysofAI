# Day 1 of my 90Day AI/ML Journey

# What to Build:
# Create a script called about_you.py that asks for name, age, height, and prints a sentence using all inputs

# 1. Get user information using input (input always returns a string)
name = input("What is your name? ").strip().title() # .strip().title() is two methods chained together that clean up and format text. .strip() removes extra spaces from beginning to end, while .title() capitalizes first letter of every word
age = input(f"Hi {name}, how old are you? ").title() # f-strings (e.g., f"Hi {name}") are the best way to insert variables.
height = input(f"{age} is great! Kindly enter your height (e.g., 6.07ft or 185cm or 1.85m): ")

# 2. Print a sentence using all inputs
print(f"Dear {name}, you are {age} years old and {height} tall.")

# Below are what I learned in order to create the script above
# comment, variables, syntax, data types (strings, integers, floats, and booleans).

# 'Comment'
# We use the hash symbol (#) for comments in python.
# in Pycharm, you can highlight a block of code and press Ctrl + / (Windows/Linux) to instantly comment it out.

# 'Variable'
# A variable is a named "container" or "placeholder" used to store data that a program can recall and use later.
# In python, you create a variable just by assigning it a value with the = sign, like x = 10.
# Basic rule:
# 1) state with a letter (a-z, A-Z) or an underscore (_)
# 2) cannot start with a number
# 3) case_sensitive
# 4) cannot use reserved keywords like if, else, while, or for as names.

# 'Syntax'
# Syntax is the blueprint of rules that ensures your code is structured correctly so the computer can understand and execute it.
# It's essentially the grammar of a programming language.

# 'Data Types'
# In Python, data types are categories that tell the computer what kind of data a value is and what you can do with it.
# Think of data types like labels on storage boxes.
# If you have a box labeled "Numbers," you know you can do math with what's inside.
# If a box is labeled "Text," you know you can read it or search for words inside it.
# The data type determines the "rules" for that variable:
# Strings are for reading and writing.
# Integers and Floats are for calculating.
# Booleans are for making decisions.
# Without data types, the computer wouldn't know the difference between the number 10 and the word "10".
# To us, they look similar, but to a computer, you can add the number 10 + 5, but you can't "mathematically add" the word "10" to a number.

# 'Data types Syntax'
# text = "Hello"  # str
# number = 10   # int
# decimal = 3.14   # float
# flag = False   # bool
# list_items = [1,2,3]   # list
# tuple_items = (1,2,3)  # tuple
# dictionary = {"key": "value"}   # dict
# unique_items = {1,2,3}  # set

# 'String'
# A string is a sequence of characters (letters, numbers, spaces, or symbols) treated as a single data type.
# Syntax: Enclosed in 'single', "double", or """triple""" quotes.
# Immutability: Cannot be modified after creation; changes result in a new string.
# Indexing: Position-based access starting from 0 (e.g., s[0]).
# Key Tools	f-strings (e.g., f"Hello {name}") are the best way to insert variables.
# user_name = "Alice" #String (text)

# 'Integer'
# Integer is a whole number with no fractional or decimal part.
# Range: Can be positive, negative, or zero.
# Limit: Practically unlimited size (restricted only by computer memory).
# Math: Supports standard math (+,-,*,/)
# Conversion: You can turn a string or decimal into an integer using int().
# user_age = 28   #Integer (whole number)

# 'Float'
# Float is a number containing a decimal component (e.g., 1.5, -0.01).
# Trigger:	Created by including a . or by using the division / operator.
# Precision:	Limited; can have small rounding errors in complex math.
# Use Cases:	Prices, percentages, temperatures, and scientific data.
# Special Values:	Can represent "Infinity" (inf) and "Not a Number" (NaN).
# hourly_rate = 35.50   #Float (decimal)

# 'Boolean'
# Boolean is a data type with only two values: True and False.
# Primary Use:	Controlling the flow of a program via Conditional Statements.
# Operators:	Uses and, or, and not to combine or flip values.
# Creation:	Result of comparisons like == (equal), != (not equal), or > (greater than).
# Casting:	The bool() function converts any value to its True/False equivalent.
# is_enrolled = True    #Boolean (True/False)


