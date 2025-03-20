import random

# Task 1: Create a list of 10 random numbers between 1 and 20
rand_list = [random.randint(1, 20) for _ in range(10)]

# Task 2: Filter Numbers Below 10 (List Comprehension)
list_comprehension_below_10 = [num for num in rand_list if num < 10]

# Task 3: Filter Numbers Below 10 (Using filter)
filter_below_10 = list(filter(lambda x: x < 10, rand_list))

# Print results
print("Random numbers:", rand_list)
print("Numbers below 10 (list comprehension):", list_comprehension_below_10)
print("Numbers below 10 (filter):", filter_below_10)
