import glob
import os
# 현재 파이썬 파일의 경로
current_path = os.path.abspath(__file__)
pdf_files = glob.glob("/Users/hidsquid97/oreumi/**/*.pdf", recursive=True)
# *: 와일드카드 문자
# **: 해당 경로 내 모든 폴더

# 파일 개수
# len(pdf_files)
