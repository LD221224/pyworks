# 리스트의 함수 사용
score = [10, 20, 30, 40, 50]

print(20 in score)  # True
print(100 in score)  # False
print(30 not in score)  # False

print("리스트의 크기 :", len(score))

# 추가
score.append(100)  # 맨 뒤에 추가
score.insert(2, 70)  # 2번 인덱스에 70 추가

# 삭제
score.pop()  # 맨 뒤 삭제
score.pop(2)  # 2번 인덱스 삭제

# 조회
for i in score:
    print(i, end=" ")
print()

# range 조회
n = len(score)
for i in range(n):
    print(score[i], end=" ")
