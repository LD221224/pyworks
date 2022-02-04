# 튜플 자료구조 예제 - 고민 상담
import random
import time

answers = (
    "자! 해보세요!",
    "됐네요, 이 사람아",
    "뭐라고? 다시 생각해보세요.",
    "모르니 두려운 것입니다."
)

print("""
안녕하세요~ Magic 상담소입니다.
조언을 구하고 싶으면 질문을 입력하고,
엔터 키를 누르세요.""")

question = input("질문 : ")
print("고민중...\n" * 4)
time.sleep(2)   # 대기시간 2초
# print(answers[1])
"""
rnd = random.randint(0, 3)
print(rnd)
print(answers[rnd])
"""

# 리스트 랜덤 선택 함수 - random.choice(리스트)
print(random.choice(answers))