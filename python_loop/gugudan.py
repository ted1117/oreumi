# 백준 연습장
# for i in range(1, 3):
#     for j in range(1, 3):
#         print(i, j)
t = int(input())

for _ in range(t):
    c_list=[25, 10, 5, 1]
    c = int(input())
    for i in c_list:
        print(c // i, end=" ")
        c %= i
