# def greet(name):
#     print("반갑습니다! {} 여러분".format(name))

# greet("oreumi")

def add(a, b):
    return a + b

def substract(a, b):
    return a- b

def multiply(a, b=2):
    return a * b

# *args는 가변인자
def sum(*args):
    total = 0
    for i in args:
        total += i
    return total
# result = multiply(3, 6)
# def database_login()
def character_info(name, age):
    print("이름:", name)
    print("나이:", age)
# result = sum(3, 6, 6, 7)
# character_info(name="김도언", age=20)
character_info(age=20, name="김도언")
# print(result)