### Exercise 6.1. ###

# Draw a stack diagram and determine program output.


def b(z):
    # Call function 'a' with arguments z, z
    prod = a(z, z)
    # Print z and prod values
    print(z, prod)
    # Return the product value
    return prod


def a(x, y):
    # Increment x by 1
    x = x + 1
    # Return the product of x and y
    return x * y


def c(x, y, z):
    # Calculate the total sum of x, y, and z
    total = x + y + z
    # Call function 'b' with the total sum and square its result
    square = b(total) ** 2
    # Return the squared result
    return square


# Initialize variables x and y
x = 1
y = x + 1
# Call function 'c' with arguments x, y+3, and x+y, then print the result
print(c(x, y + 3, x + y))

# Output Explanation:
# 1. Inside 'c': total = 1 + (2+3) + (1+2) = 9
# 2. Inside 'b': a(9, 9) = 10 * 9 = 90, prints "9 90", returns 90
# 3. Inside 'c': 90 ** 2 = 8100, which is printed as the final output
