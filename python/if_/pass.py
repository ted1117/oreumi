a = [1, 2, 3, 4, 5, 3.5, -1]
max_val = a[0]
for i in a:
    if i > max_val:
        max_val = i
        continue
print(max_val)