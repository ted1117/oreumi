f = open("/Users/hidsquid97/oreumi/python/asdf?/file_1.txt", "r")
contents = f.readlines()
# 정렬
contents.sort()
print(contents)
# 개수 세기
print(len(contents))
# 중복 제외 개수 세기
print(len(set(contents)))
f.close()