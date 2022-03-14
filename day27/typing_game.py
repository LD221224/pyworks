# 영어 타자 게임
import random
import time

try:
    # 외부의 word.txt 읽기
    f = open("./output/word.txt", 'r')
    word = f.read().split()

    # 문제 번호
    n = 1

    print('[타자 게임] 준비되면 엔터')
    input()
    start = time.time()

    while n < 11:
        # 문제
        print("문제", n)
        question = random.choice(word)
        print(question)

        # 사용자 입력
        answer = input()

        if question == answer:
            print("통과")
            # 다음 문제
            n += 1
        else:
            print("오타! 다시 도전!")

    end = time.time()
    print("타자 시간 : %.2f" % (end - start))
except:
    print("파일을 열 수 없습니다.")
