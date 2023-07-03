# def add(a, b):
#     return a + b

# add = lambda a, b: a + b
# result = add(2, 3)
# # print(result)

# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x: x**2, numbers)
# print(list(squared))

students = [
    {"name": "이민영", "age": 23},
    {"name": "양승조", "age": 17},
    {"name": "문기원", "age": 25}
]

students.sort(key=lambda x: x["age"])
students.sort(key=lambda x: x["name"])
print(students)