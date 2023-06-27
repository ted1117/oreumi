# a, b = map(int, input().split())
# # a, b = input("").split(" ")
# c, d = a, b
# while b:
#     a, b = b, a % b

# print(f"최대공약수: {a}")
# print(f"최소공배수: {c * d // a}")

n = int(input())

factors = []
while n % 2 == 0:
    factors.append(2)
    n //= 2

i = 3
while i * i <= n:
    while n % i == 0:
        factors.append(i)
        n //= i
    i += 2

if n > 1:
    factors.append(n)

print(factors)