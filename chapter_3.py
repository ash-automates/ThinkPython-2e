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


def do_twice(func, arg):
    """
    Calls the given function twice with the specified argument.

    Args:
        func: Function object to be called.
        arg: Argument to be passed to the function.
    """
    func(arg)
    func(arg)


def print_twice(s):
    """
    Prints the given string twice.

    Args:
        s (str): The string to be printed twice.
    """
    print(s)
    print(s)


# Test the do_twice function
do_twice(print_twice, "spam")


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
def do_four(func, arg):
    """
    Calls the given function four times with the specified argument.

    Args:
        func: Function object to be called.
        arg: Argument to be passed to the function.
    """
    do_twice(func, arg)
    do_twice(func, arg)


# Test the do_four function
do_four(print_twice, "spam")


# Define do_n_times function to call a function n times with a value
def do_n_times(func, arg, n):
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
do_n_times(print_twice, "spam", 7)
