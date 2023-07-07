def calculation(func):
    def wrapper(*args, **kwargs):
        print("데코레이터 1 시작")  # 1
        func(*args, **kwargs)    # calculation 2까지 종료
        print("데코레이터 1 종료")  # 3
    return wrapper

def calculation2(func):
    def wrapper(*args, **kwargs):
        print("데코레이터 2 시작")  # 2
        func(*args, **kwargs)
        print("데코레이터 2 종료")  # 4
    return wrapper

# 액자식 구성으로 작동
@calculation
@calculation2
def add(a,b):
    print(a + b)

add(3, 5)