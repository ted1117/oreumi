n = int(input())
curr_val = 1
next_val = 1
for i in range(n-2):
    tmp = next_val
    next_val += curr_val
    curr_val = tmp
print(f"{n}번째: {next_val}")