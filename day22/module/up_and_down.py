import random as r

# 난수 저장(1 ~ 100)
com = r.randint(1, 100)
min_v = 1   # 최솟값
max_v = 100 # 최댓값

for i in range(10):
    guess = int(input("맞혀보세요[%d회](%d ~ %d) : " % (i + 1, min_v, max_v)))
    if guess == com:
        print("정답!")
        break
    elif guess > com:
        print("너무 커요")
        max_v = guess   # 최댓값 변경
    else:
        print("너무 작아요")
        min_v = guess   # 최솟값 변경

print("점수 : %d점" % ((10 - i) * 10))