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
