import re

# 정규표현식
pattern1 = re.compile('[a-z]+')
result = pattern1.match("before")
print(result)

pattern2 = re.compile('[0-9]+\s[a-z]+')
result2 = pattern2.match("2022 python")
print(result2)
