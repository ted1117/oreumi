# n = int(input())
# val_5 = n // 5
# flag = 1
# while True:  
#     if (n - (val_5 * 5)) % 3 == 0:
#         val_3 = (n - (val_5 * 5)) // 3
#         break
#     val_5 -= 1
#     if val_5 < 0:
#         flag = 0
# print(val_5 + val_3 if flag else -1)
import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.sort()
print(*a, sep="\n")