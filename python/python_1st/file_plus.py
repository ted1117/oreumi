file = open("/Users/hidsquid97/oreumi/python_1st/context2.txt", "a+")
# context = file.read()
# print(context)
file.write("content")
file.close()

file = open("/Users/hidsquid97/oreumi/python_1st/context3.txt", "a")
file.write("content")
file.close()