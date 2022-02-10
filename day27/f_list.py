# 파일에 리스트 쓰기
season = ['봄', '여름', '가을', '겨울']

f = open('c:/pyfile/season.txt', 'w')

"""
for i in season:
    f.write(i + '\n')
"""

for i in range(0, len(season)):
    f.write(season[i] + '\n')

f.close()

# 파일 읽기
try:
    f = open('c:/pyfile/season.txt', 'r')
    season = f.read()
    print(season)
    f.close()
except:
    print("파일을 열 수 없습니다.")