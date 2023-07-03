"""
일급함수
"""

# def cat():
#     return "Meow"

# dog = cat
# print(dog())
def apply_operation(func, x, y):
    return func(x, y)

# 가변 인자 이용
# def apply_operation(func, *args):
#     return func(*args)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

result = apply_operation(add, 2, 3)
result = apply_operation(sub, 2, 3)
result = apply_operation(mul, 2, 3)
print(result)