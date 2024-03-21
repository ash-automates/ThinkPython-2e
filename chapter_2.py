### Exercise 2.1. ###

# Question 1: We've seen that n = 42 is legal. What about 42 = n?
# In Python, variable assignment follows the pattern variable = value.
# Assigning a value to a literal like 42 = n is not allowed and will result in a SyntaxError.

n = 42  # This assigns the value 42 to the variable n
# 42 = n  # Uncommenting this line will result in a SyntaxError


# Question 2: How about x = y = 1?
# Python allows chaining assignment statements, where multiple variables can be assigned the same value in a single line.

x = y = 1  # Both x and y are assigned the value 1 simultaneously
print(x)  # Output: 1
print(y)  # Output: 1


# Question 3: What happens if you put a semi-colon at the end of a Python statement?
# In Python, using a semi-colon at the end of a statement is valid but not commonly used as in some other languages.
# It allows writing multiple statements in a single line, but it's not considered Pythonic.

print("Hello")
# This is a valid but uncommon way to end a statement


# Question 4: What if you put a period at the end of a statement?
# Putting a period at the end of a statement is invalid syntax in Python and will result in a SyntaxError.

# print("Hello").  # Uncommenting this line will result in a SyntaxError


# Question 5: What happens if you try to multiply x and y like this: xy?
# In Python, expressions must have an operator between variables or literals to perform calculations.
# Attempting to use variable names directly without an operator will result in a NameError.

x = 5
y = 10
# z = xy  # Uncommenting this line will result in a NameError because Python expects an operator between x and y

### Exercise 2.2. ###

# Exercise 2.2: Practice using the Python interpreter as a calculator

import datetime

# Question 1: Volume of a sphere with radius 5
radius = 5
volume = (4/3) * 3.14159 * (radius ** 3)
print(f"Volume of a sphere with radius 5 is {volume:.2f} cubic units.")

# Question 2: Total wholesale cost for 60 copies of a book
cover_price = 24.95  # in dollars
discount_rate = 0.4  # 40% discount
shipping_first_copy = 3  # in dollars
shipping_additional_copy = 0.75  # in dollars

# Calculate total cost for 60 copies with discount and shipping
total_cost = (cover_price * (1 - discount_rate) * 60) + shipping_first_copy + (59 * shipping_additional_copy)
print(f"Total wholesale cost for 60 copies is ${total_cost:.2f}.")

# Question 3: Calculate time to get home for breakfast
start_time = datetime.datetime(1, 1, 1, 6, 52)  # 6:52 am
easy_pace = datetime.timedelta(minutes=8, seconds=15)  # 8:15 per mile
tempo_pace = datetime.timedelta(minutes=7, seconds=12)  # 7:12 per mile

# Calculate total running time
total_running_time = (2 * easy_pace) + (3 * tempo_pace)

# Add running time to start time to get home time
home_time = start_time + total_running_time
print(f"I will get home for breakfast at {home_time.strftime('%I:%M %p')}.")

# Output:
# Volume of a sphere with radius 5 is 523.60 cubic units.
# Total wholesale cost for 60 copies is $945.45.
# I will get home for breakfast at 07:30 AM.
