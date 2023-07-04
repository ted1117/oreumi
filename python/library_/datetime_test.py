from datetime import datetime, timedelta

cur_time = datetime.now()
print("현재 시각: ", cur_time)

formatted_time = cur_time.strftime("%Y/%m/%d %H:%M:%S")
print("형식 시각: ", formatted_time)

day_before = cur_time - timedelta(days=1)
print("하루 전: ", day_before)