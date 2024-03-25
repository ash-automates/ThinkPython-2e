### Exercise 4.1. ###

import time


def print_hms_from_epoch(epoch_time):
    # Calculate the number of hours from the epoch time
    epoch_hours = int(epoch_time) // 3600

    # Calculate the remaining seconds after extracting hours
    leftovers = int(epoch_time) % 3600

    # Calculate the number of minutes from the remaining seconds
    epoch_minutes = leftovers // 60

    # Calculate the number of seconds from the remaining seconds
    epoch_seconds = leftovers % 60

    # Print the formatted time string using the format operator (%)
    print("The time now is %d:%d:%d" % (epoch_hours, epoch_minutes, epoch_seconds))


# Get the current epoch time using time.time() and print the hours, minutes, and seconds
print_hms_from_epoch(time.time())
