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
