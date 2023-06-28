# a = [x for x in range(1, 6)]

# remove
# 중복된 요소가 있다면 인덱스가 낮은 요소 삭제
# a.remove(3)

# pop
# 인자는 인덱스, 기본값은 마지막 인덱스

# 정렬
# b = [5, 3, 2, 4, 6, 1]
# b.sort()
# 역순
# b.sort(reverse=True)
# print(b)

# extend
a = [1, 2, 3]
b = [4, 5, 6]

# a.extend(b)
# print(a)

# a += b
# print(a)
# a *= 3
# print(a)

# a.insert(-1, 4)
# print(a)

# pop
# a.pop(2)
# print(a)

# index 출력
print(a.index(1))

# count: 해당 요소의 수 세기
print(a.count(1))

# reverse: 리스트 요소 역순 (크기와 상관 없음)
# a.reverse()

# n = int(input())
# for idx, i in enumerate(a):
#     if i == n:
#         print(idx)
# print(a.index(n))

point = 1, 2
print(type(point))
x, y = point
print(x, y)

# dict
