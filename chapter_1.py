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

### Exercise 1.2. ###

# Question 1: How many seconds are there in 42 minutes 42 seconds?
# We can calculate this by converting 42 minutes to seconds and then adding
# the remaining 42 seconds.
minutes = 42
seconds = 42
total_seconds = (minutes * 60) + seconds
print(f"There are {total_seconds} seconds in 42 minutes 42 seconds.")

# Output:
# There are 2562 seconds in 42 minutes 42 seconds.

# Question 2: How many miles are there in 10 kilometers? Hint: there are
# 1.61 kilometers in a mile.
# We can use the conversion factor provided to convert kilometers to miles.
kilometers = 10
miles = kilometers / 1.61
print(f"There are {miles} miles in 10 kilometers.")

# Output:
# There are 6.211180124223602 miles in 10 kilometers.

# Question 3: If you run a 10 kilometer race in 42 minutes 42 seconds,
# what is your average pace (time per mile in minutes and seconds)?
# What is your average speed in miles per hour?
race_distance_km = 10
race_time_minutes = 42
race_time_seconds = 42

# Calculate total race time in minutes
total_race_time_minutes = race_time_minutes + (race_time_seconds / 60)

# Calculate pace per mile in minutes and seconds
pace_per_mile_minutes = total_race_time_minutes / miles
pace_per_mile_seconds = (pace_per_mile_minutes - int(pace_per_mile_minutes)) * 60

# Calculate average speed in miles per hour
average_speed_mph = miles / (total_race_time_minutes / 60)

# Print the results
print(f"Your average pace is {int(pace_per_mile_minutes)} minutes and {int(pace_per_mile_seconds)} seconds per mile.")
print(f"Your average speed is {average_speed_mph} miles per hour.")

# Output:
# Your average pace is 6 minutes and 52 seconds per mile.
# Your average speed is 8.727653570337614 miles per hour.
