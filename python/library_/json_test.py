import json

with open("/Users/hidsquid97/oreumi/python/library_/password.json", "r") as f:
    json_data = json.load(f)

print(json_data["password"])
json_data["delivery"] = "만두"

with open("/Users/hidsquid97/oreumi/python/library_/password.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False)