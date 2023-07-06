import re

# pattern = r"b.t"
# string = "bat, but, bit, bet, baat"

# pattern = r"ab+c"
# string = "ababc"

# pattern = r"ab*c"
# string = "ac, abc, abbc, abbbc, abdc"

# pattern = r"(ab)+
# string = "abc, ababc, abababc, ab, aabbc"

# pattern = r"\d+"
# string = "I have 10 appes and 5 bananas"

# pattern = r\w+"
# string = "Hello, world! 123"

# pattern = r"^Hello"
# pattern = r"hon!$"
# string = "Hello, World! Hello, Python!"

# pattern = r"[ab]" # == r"a|b"
# string = "ab, abc, aabc, aaabc"

# pattern = r"(ab)+"
# string = "ababc"

# result = re.match(pattern, string)
# print(result)
# print(result.group())

# string = "나의 전화번호는 010-1234-5678입니다. 다른 번호로는 02-987-6543입니다."
# pattern = r"[0-9-]+"
# result = re.findall(pattern, string)
# print(result)

# string = "나의 전화번호는 !-010-1234-5678-!입니다. 다른 번호로는 !-02-987-6543-!입니다. 125!22%13. 지역번호가 155542-10-1"
# pattern = r"[0-9]{2,4}+-[0-9]{2,4}+-[0-9]{2,4}+"
# result = re.findall(pattern, string)
# print(result)

# string = "안녕하세요. 이메일 주소는 abc@example.com입니다. 다른 이메일은 ab_TE@hcu.co.kr이고, x_yz@hotmail.net도 있습니다."
# pattern = r"\S+@[a-z.]+"
# result = re.findall(pattern, string)
# print(result)

string = "문장 속에는 다양한 URL이 있습니다. https://www.example.com/, http://subdomain.example.co.kr/, www.google.com, ftp://fileserver.example.org, 이렇게 다양한 형식의 URL이 있습니다."
pattern = r"[a-z0-9.:/-]+[0-9a-z.]+[a-z./]+"
result = re.findall(pattern, string)
result = re.sub(pattern, "", string)
print(result)