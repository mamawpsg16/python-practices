credits = [100, 200, 300]

# MAP
doubled_credits = list(map(lambda x: x * 2, credits))
print(doubled_credits)

# FILTER
filtered_credits = list(filter(lambda x: x > 100, credits))
print(filtered_credits)

# reduce
from functools import reduce
total_credits = reduce((lambda x, y: x + y), credits)
print(total_credits)