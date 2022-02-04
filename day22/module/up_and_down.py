import random as r

# 난수 저장(1 ~ 100)
com = r.randint(1, 100)
min_v = 1   # 최솟값
max_v = 100 # 최댓값

for i in range(10):
    try:    # 문자 입력시 오류처리(try: ~ except ValueError: ~)
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
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력하세요.")

print("점수 : %d점" % ((10 - i) * 10))