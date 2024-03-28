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

### Exercise 6.2. ###

# Ackermann function implementation and evaluation.


def ack(m, n):
    """Compute the Ackermann function A(m, n)."""
    # Base case: if m = 0, return n + 1
    if m == 0:
        return n + 1
    # Recursive case: if n = 0, call ack(m-1, 1)
    elif n == 0:
        return ack(m - 1, 1)
    # Recursive case: use ack(m-1, ack(m, n-1))
    else:
        return ack(m - 1, ack(m, n - 1))


# Evaluate ack(3, 4) as an example
print("Ackermann(3, 4) =", ack(3, 4))

# What happens for larger values of m and n?
# Note: The Ackermann function grows extremely fast, leading to stack overflow errors for large inputs.
# Uncomment the below line to see this behavior (caution: may cause stack overflow).
# print("Ackermann(3, 7) =", ack(3, 7))
