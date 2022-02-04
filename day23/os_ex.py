# os 모듈 사용하기
# 환경변수나 디렉터리, 파일 등의 os 자원을 제어하는 모듈
import os

# 경로 이동
os.chdir('c:/pyworks/day20')

# dir 명령 실행
dir = os.popen('dir')

print(dir.read())
