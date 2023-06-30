answer = 20

while True:
    a = int(input())
    
    if a < answer:
        print("업")
    elif a > answer:
        print("다운")
    else:
        print("정답!")
        break