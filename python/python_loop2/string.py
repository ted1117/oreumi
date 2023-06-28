text = "Hello World!"
a = []
for i in text:
    a.append(i)
print(a)
b = [x for x in text]
print(b)
c = list(text)
print(c)

print("".join(a))

a = ["안녕", "오늘도", "수고했어", "!"]
print("\n".join(a))