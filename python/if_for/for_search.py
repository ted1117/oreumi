numbers = [1, 2, 3, 4, 5, 6]

# O(n)
sum = 0
for i in numbers:
    sum += i

# O(1)
sum = (numbers[5] + 1) * len(numbers) / 2