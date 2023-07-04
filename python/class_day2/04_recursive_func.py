def factorial(n):
    return n * factorial(n-1) if n > 0 else 1

def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n-2) if n > 1 else n

for i in range(5):
    print(fibonacci(i))