text = b'\xbc\xd3\xd3\xcd'

import codecs

# result = codecs.decode(text, encoding="utf-8")
# print(result)
# print(text.decode("euc-kr"))
result = codecs.decode(text, encoding="euc-kr")
result = codecs.decode(text, encoding="gb2312")
print(result)

with open("/Users/hidsquid97/oreumi/python/python_final/codec_list.txt", "r") as f:
    codec_list = f.read().replace(",", "").replace("\n", " ").replace("  ", " ").split("\n")
# print(codec_list)

for codec in codec_list:
    try:
        print(text.decode(codec), codec)
    except:
        pass