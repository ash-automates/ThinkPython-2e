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
