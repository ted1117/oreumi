n = int(input())

# 소수 판별 플래그
is_prime = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print("Nope")
        is_prime = False
        break
else:
    print("Yup")
# if is_prime:
#     print("Yup")