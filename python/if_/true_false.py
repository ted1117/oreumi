def func() -> None:
    pass

# a = func()
a, b = 1, 1

# is는 값을 비교하지 않고 자료의 메모리 주소를 비교한다.
# ==는 값을 비교한다.
if a is b:
    print("True")
else:
    print("False")

