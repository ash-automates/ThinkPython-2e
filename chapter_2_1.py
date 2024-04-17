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
