# None
print(type(None))

# Bool
print(type(True), type(False))

# 숫자형
print(type(5), type(3.14))
print(type(2 + 3j))

# 문자형
print(type("아무거나"))

# 시퀀스
print(type((1, 2, 4)))
print(type([1, 2, 4]))

# dict
print(type({"A": 12, "B": 13}))

# set
print(type({1, 2, 4}))

# function
def foo():
    pass
print(type(foo))

# 형 변환
a = 2
print(type(int(a)))