### Exercise 1.1. ###

# Question 1: In a print statement, what happens if you leave out one of the
# parentheses, or both? Let's try it out:
print("Hello"  # Missing closing parenthesis
print "Hello"  # Missing both opening and closing parentheses

# Question 2: If you are trying to print a string, what happens if you leave out
# one of the quotation marks, or both? Let's try it out:
print("Hello)  # Missing closing quotation mark
print(Hello")  # Missing opening quotation mark

# Question 3: You can use a minus sign to make a negative number like -2.
# What happens if you put a plus sign before a number? What about 2++2?
# Let's try it out:
print(+2)      # Adding a plus sign before a number is redundant, it doesn't
               # change the value
print(2++2)    # This is equivalent to 2 + (+2), which results in 4

# Question 4: In math notation, leading zeros are ok, as in 09.
# What happens if you try this in Python? What about 011? Let's try it out:
print(09)      # This will raise a SyntaxError because leading zeros are not
               # allowed in Python integers
print(011)     # This will also raise a SyntaxError for the same reason

# Question 5: What happens if you have two values with no operator between them?
# Let's try it out:
print(2 3)     # This will raise a SyntaxError because there is no operator
               # between the two values

"""Explanation and Comments:

1. Missing parentheses in a print statement will result in a SyntaxError
because Python expects the syntax to be correct.
2. Missing quotation marks in a string will also result in a SyntaxError
because Python expects string literals to be enclosed in quotes.
3. Adding a plus sign before a number doesn't change its value; it's simply
redundant. 2++2 is parsed as 2 + (+2) which is 4.
4. Python does not allow leading zeros in integer literals because it
interprets them as octal literals. Use base 10 integers without leading zeros.
5. Python requires an operator between two values for an expression to be
valid. Without an operator, it's a syntax error.
"""
