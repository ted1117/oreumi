file = open("/Users/hidsquid97/oreumi/python_1st/byte.txt", "rb")
context = file.read()
print(context)
file.close()

file = open("/Users/hidsquid97/oreumi/python_1st/byte.txt", "wb")
file.write(b"hello")
file.close()