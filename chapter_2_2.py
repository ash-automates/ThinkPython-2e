import datetime

# Question 1: Volume of a sphere with radius 5
radius = 5
volume = (4/3) * 3.14159 * (radius ** 3)
print(f"Volume of a sphere with radius 5 is {volume:.2f} cubic units.")

# Question 2: Total wholesale cost for 60 copies of a book
cover_price = 24.95  # in dollars
discount_rate = 0.4  # 40% discount
shipping_first_copy = 3  # in dollars
shipping_additional_copy = 0.75  # in dollars

# Calculate total cost for 60 copies with discount and shipping
total_cost = (cover_price * (1 - discount_rate) * 60) + shipping_first_copy + (59 * shipping_additional_copy)
print(f"Total wholesale cost for 60 copies is ${total_cost:.2f}.")

# Question 3: Calculate time to get home for breakfast
start_time = datetime.datetime(1, 1, 1, 6, 52)  # 6:52 am
easy_pace = datetime.timedelta(minutes=8, seconds=15)  # 8:15 per mile
tempo_pace = datetime.timedelta(minutes=7, seconds=12)  # 7:12 per mile

# Calculate total running time
total_running_time = (2 * easy_pace) + (3 * tempo_pace)

# Add running time to start time to get home time
home_time = start_time + total_running_time
print(f"I will get home for breakfast at {home_time.strftime('%I:%M %p')}.")

# Output:
# Volume of a sphere with radius 5 is 523.60 cubic units.
# Total wholesale cost for 60 copies is $945.45.
# I will get home for breakfast at 07:30 AM.
