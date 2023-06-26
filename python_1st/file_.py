# fp = "/Users/hidsquid97/oreumi/python_1st/title.txt"
# file = open(fp, "r")

# content = file.read()
# print(content)

# file.close()

fp = "/Users/hidsquid97/oreumi/python_1st/context.txt"
# r은 읽기, w는 쓰기, a는 추가
file = open(fp, "w")

file.write("test context. Another context.")

file.close()