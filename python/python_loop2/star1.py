n = int(input())
'''
for i in range(1, n+1):
    print("*" * i)
    '''
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()