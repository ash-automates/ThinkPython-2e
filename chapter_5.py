### Exercise 5.1. ###

import time


def print_hms_and_de(epoch_time):
    """
    Calculate and print the current time in hours, minutes, seconds,
    and the number of days elapsed since the epoch.

    Args:
    - epoch_time (float): The epoch time to convert and print.

    Returns:
    None
    """
    # Calculate the number of hours, minutes, and seconds
    epoch_hours = int(epoch_time) // 3600
    leftovers = int(epoch_time) % 3600
    epoch_minutes = leftovers // 60
    epoch_seconds = leftovers % 60

    # Calculate the number of days elapsed
    days_elapsed = int(epoch_time / (60 * 60 * 24))

    # Print the formatted time string using the format operator (%)
    print(
        "The time now is %d:%d:%d | %d days elapsed since epoch!"
        % (epoch_hours, epoch_minutes, epoch_seconds, days_elapsed)
    )


# Get the current epoch time using time.time()
current_epoch_time = time.time()

# Print the current epoch time
print("Current Epoch Time:", current_epoch_time)

# Print the current time in hours, minutes, seconds, and days elapsed
print_hms_and_de(current_epoch_time)

### Exercise 5.2. ###

# Checking Fermat's Last Theorem

def check_fermat(a, b, c, n):
    """
    Check if Fermat's Last Theorem holds for given values of a, b, c, and n.

    Parameters:
    - a, b, c: Positive integers
    - n: Integer greater than 2
    """
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def get_fermat_inputs():
    """
    Prompt the user to input values for a, b, c, and n, and convert them to integers.

    Returns:
    - Tuple containing a, b, c, n (positive integers and n > 2)
    """
    a = int(input("Enter a positive integer value for a: "))
    b = int(input("Enter a positive integer value for b: "))
    c = int(input("Enter a positive integer value for c: "))
    n = int(input("Enter a positive integer value for n (greater than 2): "))
    return a, b, c, n

# Example usage
check_fermat(3, 4, 5, 6)  # Testing the function with predefined values

# Prompting user for input and checking Fermat's Last Theorem
# The star operator (*) unpacks the tuple returned by get_fermat_inputs()
check_fermat(*(get_fermat_inputs()))
