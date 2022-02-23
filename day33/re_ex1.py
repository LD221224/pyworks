import re

# 정규표현식
str = "before"
pattern1 = re.compile('[a-z]+')
result = pattern1.match(str)
print(result)
# group() - 문자열로 반환
print(result.group())
# start() - 시작 인덱스 반환
print(result.start())
# span() - 튜플(시작, 끝 인덱스)
print(result.span())

pattern2 = re.compile('[0-9]+\s[a-z]+')
result2 = pattern2.match("2022 python")
print(result2)
print(result2.group())
# start() - 끝 인덱스 반환
print(result2.end())
