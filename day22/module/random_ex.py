import math
import random
# 0 <= random.random() < 1.0
print(random.random())

# 1 ~ 10 무작위 수 - math, random 사용
num = math.floor(random.random() * 10) + 1
print(num)

# 1 ~ 10 무작위 수 - random 사용
num2 = random.randint(1, 10)
print(num2)

# 주사위
dice = random.randint(1, 6)
print(dice)

# 리스트 요소 무작위 추출
동물 = ['호랑이', '소', '강아지', '고양이', '닭']
idx = math.floor(random.random() * len(동물))
print(동물[idx])

# random.choice(리스트)
print(random.choice(동물))

# 리스트 요소 섞기
random.shuffle(동물)
print(동물)
