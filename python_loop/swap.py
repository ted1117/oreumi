a = list(range(1, 6))
'''
# reverse 함수
a.reverse()
print(a)

# 인덱스 슬라이싱
b = a[::-1]
print(b)

# 반복문
a.reverse() # 리스트 되돌리기
print(a)
# while 반복문
left = 0
right = len(a) - 1

while left < right:
    a[left], a[right] = a[right], a[left]
    left += 1
    right -= 1
print(a)
'''
b = ["a", "b", "c", "d", "e", "f"]
for i, j in enumerate(b):
    print(i, j)