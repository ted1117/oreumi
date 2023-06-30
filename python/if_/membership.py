fav_fruits = ["사과", "수박", "배"]
mom_fruits = ["멜론", "수박", "배", "딸기"]

eat_list = [x for x in mom_fruits if x in fav_fruits]
eat_list1 = []
for fruit in mom_fruits:
    if fruit in fav_fruits:
        print(f"{fruit} 먹는다!")
        eat_list1.append(fruit)
    else:
        print(f"{fruit} 안 먹는다!")
print(eat_list)
print(eat_list1)