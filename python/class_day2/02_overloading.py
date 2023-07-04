def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c

# 동일한 이름으로 서로 다른 매개변수를 가진 함수를 여러 개 사용
# python에선 overload를 지원하지 않음
print(add(2, 3, 4))
