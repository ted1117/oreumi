# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))

def outer():
    x = 10
    def inner():
        print(x)
    inner()

# 내부 함수는 외부에서 접근 불가
