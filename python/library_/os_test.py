import os

forlder_path = "/Users/hidsquid97/oreumi"

if os.name == "nt":
    forlder_path = "/Users/hidsquid97/oreumi"
elif os.name == "posix":
    forlder_path = "/Users/hidsquid97/oreumi"
if not os.path.exists(forlder_path):
    os.makedirs(forlder_path)
    print(f"폴더 {forlder_path}를 생성했습니다.")
else:
    print(f"폴더 {forlder_path}가 존재합니다.")