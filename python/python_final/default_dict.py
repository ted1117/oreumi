from collections import defaultdict

my_dict = defaultdict(int)  # dict 생성 후 모든 value를 0으로 초기화

my_dict["사과"] += 1
my_dict["바나나"] += 1
my_dict["수박"] += 1

# print(my_dict)

text = "나, 는 사과, 를, 먹기, 위해서, 사과, 를, 했습니다."

my_dict = defaultdict(int)

word_list = list(map(lambda x: x.replace(",", ""), text.split()))

for word in word_list:
    my_dict[word] += 1

print(my_dict)