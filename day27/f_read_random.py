import random
# split() - 구분 기호로 분리해 리스트로 반환

f = open('c:/pyfile/season.txt', 'r')
# 공백문자로 데이터를 분리해 리스트로 반환
season = f.read().split()
print(season)
# print(season[1])
word = random.choice(season)
print(word)
f.close()