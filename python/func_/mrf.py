"""
map, reduce, filter
"""
# map(func, list or tuple)
# reduce
from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# sum = reduce(lambda x, y: x + y, numbers)
# print(sum)

# filter
# numbers = [1, 2, 3, 4, 5]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)
# even = [x for x in numbers if x % 2 == 0]
# print(even)

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

# factorial
factorial = reduce(lambda x, y: x * y, numbers)
print(factorial)

numbers = ["letter", "bigger"]
print(*list(map(lambda x: x.upper(), numbers)))