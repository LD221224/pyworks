# 최고 점수와 위치

# 점수 리스트 생성
score = [70, 80, 20, 90, 100, 50]

# 최고 점수
max_v = score[0]
for i in score:
    if max_v < i:
        max_v = i
        
print("최고 점수 :", max_v)

# 내장 함수 max(), min()
print("최고 점수 :", max(score))
print("최저 점수 :", min(score))

# 최고 점수 위치
max_idx = 0
n = len(score)
for i in range(1, n):
    if score[max_idx] < score[i]:
        max_idx = i

print("최고 점수 위치 :", max_idx)
