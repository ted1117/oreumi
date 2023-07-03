numbers = [1, 2, 3, 4, 5]
result = [x for x in numbers if x % 2 == 0]
a = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(a)
print(result)