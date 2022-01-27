# 튜플의 생성 및 사용

t1 = (1,)   # 1개 저장할 때 콤마(,)를 뒤에 붙임
t2 = (2, 3, 4)
t3 = t1 + t2

# 출력
print(t1)
print(t2)
print(t3)

# 인덱싱과 슬라이싱
print(t3[0])
print(t3[:2])
print(t3[2:])

# 수정 - 불가
# t3[1] = 5
# TypeError: 'tuple' object does not support item assignment

# 삭제 - 불가
# del t3[2]
# TypeError: 'tuple' object doesn't support item deletion
