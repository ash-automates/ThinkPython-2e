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


### Exercise 6.3. ###

def first(word):
    """Returns the first character of a string."""
    return word[0]


def last(word):
    """Returns the last character of a string."""
    return word[-1]


def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]


def is_palindrome(word):
    """
    Checks if a word is a palindrome recursively.

    Args:
    - word (str): The word to check.

    Returns:
    - bool: True if the word is a palindrome, False otherwise.
    """
    if len(word) <= 1:  # Base case: empty string or single character is a palindrome
        return True
    if first(word) != last(word):  # If first and last characters are not equal, not a palindrome
        return False
    return is_palindrome(middle(word))  # Recursive call to check the middle part


# Testing the functions
print(is_palindrome('noon'))  # True
print(is_palindrome('redivider'))  # True
print(is_palindrome('hello'))  # False

# Additional testing
print(is_palindrome('a'))  # True (single character is a palindrome)
print(is_palindrome(''))  # True (empty string is a palindrome)

### Exercise 6.4. ###

def is_power(a, b):
    """
    Checks if a is a power of b using recursion.

    Args:
    - a (int): The number to check.
    - b (int): The base.

    Returns:
    - bool: True if a is a power of b, False otherwise.
    """
    if a == b:  # Base case: a is already equal to b, hence a is a power of b
        return True
    elif a % b == 0 and a != 0:  # Check if a is divisible by b and not zero
        return is_power(a / b, b)  # Recursively check if a/b is a power of b
    else:
        return False

# Test cases
print(is_power(256, 2))  # True (256 is 2^8)
print(is_power(1024, 2))  # True (1024 is 2^10)

### Exercise 6.5. ###

def gcd(a, b):
    """
    Finds the greatest common divisor (GCD) of two numbers using recursion.

    Args:
    - a (int): First number.
    - b (int): Second number.

    Returns:
    - int: The GCD of a and b.
    """
    if b == 0:  # Base case: If b is 0, GCD is a
        return a
    else:
        return gcd(b, a % b)  # Recursively call gcd with b and the remainder of a/b

# Test cases
print(gcd(10, 45))  # Expected output: 5
print(gcd(1701, 3768))  # Expected output: 3
print(gcd(60, 48))  # Expected output: 12
print(gcd(81, 27))  # Expected output: 27
