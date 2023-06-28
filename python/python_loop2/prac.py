# import sys

# n = int(sys.stdin.readline().rstrip())

# for i in range(1, 2*n):
#     if i <= n:
#         print("*" * i + " " * (2*(n-i)) + "*" * i)
#     else:
#         print("*" * (2*n-i) + " " * 2*(i-n) + "*" * (2*n-i))
# n = int(input())
# if n == 1:
#     print("*")
# else:
#     for i in range(1, n+1):
#         print(" " * (n-i) + "*" + " *" * (i-1))
n = int(input())
if n == 1:
    print("*")
else:
    for i in range(1, n):
        if i == 1:
            print(' '* abs(n-i) + '*')
            continue
        print(' '* abs(n-i) + '*' + " " * (2*i-3) + "*")
    print("*" * (2*n-1))



    

