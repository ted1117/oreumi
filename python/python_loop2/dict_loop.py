a = {"이름": "asuna", "나이": 17, "직업": "학생", "일일퀴즈성적": [10, 20, 30]}
b = {"이름": "yuuka", "나이": 17, "직업": "학생", "일일퀴즈성적": [30, 40, 50]}
c = {"전화번호": "010-1234-5678", "주소": "인천"}
# print(type(a.items()))
# for key, value in a.items():
#     print(key, value)

# print()
# # key만 출력
# for key in a.keys():
#     print(key)

# # 리스트에 value 추가
# c = []
# for value in a.values():
#     c.append(value)
# print(c)
# # 더 짧은 방법
# d = list(a.values())
# print(d)

# 딕셔너리 합치기
a.update(c)
print(a)

