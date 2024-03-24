### Exercise 3.1. ###

# Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is in column 70
# of the display.


def right_justify(word: str):
    """
    Prints the given word with leading spaces to right-justify it in a 70-column display.

    Args:
        word (str): The word to be right-justified.
    """
    spaces_needed = 70 - len(word)  # Calculate the number of spaces needed
    print(" " * spaces_needed + word)  # Print the word with leading spaces


# Test cases
right_justify("cat")
right_justify("bulldog")
right_justify("extravagant")


### Exercise 3.2. ###


# Implementing do_twice, print_twice, do_four, and do_n_times functions


def do_twice(func):
    """
    Calls the given function twice with the specified argument.

    Args:
        func: Function object to be called.
    """
    func()
    func()


def print_twice(s):
    """
    Prints the given string twice.

    Args:
        s (str): The string to be printed twice.
    """
    print(s)
    print(s)


# Modified do_twice function to take a value and call the function twice with the value
def do_twice_with_value(func, arg):
    """
    Calls the given function twice with the specified argument.

    Args:
        func: Function object to be called.
        arg: Argument to be passed to the function.
    """
    func(arg)
    func(arg)


# Test the modified do_twice_with_value function
do_twice_with_value(print_twice, "spam")


# Define do_four function to call a function four times with a value
def do_four(func):
    """
    Calls the given function four times with the specified argument.

    Args:
        func: Function object to be called.
    """
    do_twice(func)
    do_twice(func)


# Define do_four function to call a function four times with a value
def do_four_with_value(func, arg):
    """
    Calls the given function four times with the specified argument.

    Args:
        func: Function object to be called.
    """
    do_twice_with_value(func, arg)
    do_twice_with_value(func, arg)


# Test the modified do_four_with_value function
do_four_with_value(print_twice, "spam")


# Define do_n_times function to call a function n times with a value
def do_n_times(func, n, arg):
    """
    Calls the given function n times with the specified argument.

    Args:
        func: Function object to be called.
        arg: Argument to be passed to the function.
        n (int): Number of times to call the function.
    """
    for i in range(n):
        func(arg)


# Test the do_n_times function
do_n_times(print_twice, 7, "spam")


### Exercise 3.2. ###


def print_beam():
    print("+ - - - -", end=" ")  # Print a horizontal beam of the grid


def print_post():
    print("|        ", end=" ")  # Print a vertical post of the grid


def print_beams():
    """
    Prints the top and bottom beams of a row in the grid.
    """
    do_twice(print_beam)  # Print two horizontal beams
    print("+")  # Print the closing plus sign of the row


def print_posts():
    """
    Prints the vertical posts of a row in the grid.
    """
    do_twice(print_post)  # Print two vertical posts
    print("|")  # Print the closing vertical post of the row


def print_row():
    """
    Prints a single row of the grid.
    """
    print_beams()  # Print the top and bottom beams of the row
    do_four(print_posts)  # Print four vertical posts of the row


def print_grid():
    """
    Prints a 2x2 grid using rows and columns.
    """
    do_twice(print_row)  # Print two rows of the grid
    print_beams()  # Print the final bottom beams to complete the grid


# Test the print_grid function to see the grid output
print_grid()
