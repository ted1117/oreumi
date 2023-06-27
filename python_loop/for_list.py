# 과일 출력
# f = ["사과", "딸기", "수박", "키위"]
# for x in f:
#     print(x)

# range
# for i in range(5):
#     print(i)

f = ["사과", "딸기", "수박", "키위"]
prices = [2500, 15000, 5000]
amounts = [5, 6, 3]
# enumerate
# for idx, x in enumerate(f):
#     print(idx+1, x)

# zip
for fruit, price, amount in zip(f, prices, amounts):
    profit = price * amount
    print(fruit, price, amount, profit)

# reversed
# a = [1, 2, 3]
# for i in reversed(a):
#     print(i)

# with open("/Users/hidsquid97/oreumi/python_loop/test.txt", "r") as f:
#     text = f.read().split("\n")
#     for idx, line in enumerate(text):
#         name, score = line.split(" ")
#         print(f"{idx+1}번째 학생: {name}, 점수: {score}")

# len() 없이 문자열 수 세기
# a = "Hello World!"
# cnt = 0
# for i in a:
#     cnt += 1
# print(cnt)
# print(len(a))

# sum() 없이 리스트 안의 요소 모두 더하기
# a = [1, 2, 3, 4, 5]
# hap = 0
# for i in a:
#     hap += i
# print(hap)

# def factorial(n) -> int:
#     return n * factorial(n-1) if n > 1 else 1

# print(factorial(5))

# for 반복문으로 factorial 구하기
# a = int(input("팩토리얼 입력: "))
# factorial = 1
# for i in range(1, a+1):
#     factorial *= i

# print(factorial)

# 최대공약수 구하기
