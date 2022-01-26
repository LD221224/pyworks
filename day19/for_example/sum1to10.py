# 1부터 10까지 합계
sum_v = 0
for i in range(1, 11):
    sum_v += i
    print("i =", i, ", sum_v =", sum_v)
print("합계 :", sum_v)
print()

# 1부터 입력 받은 n까지 합계
n = int(input("숫자 입력 : "))
sum_v = 0
for i in range(1, n + 1):   # + 1 주의
    sum_v += i
print("합계 :", sum_v)

"""
# 1부터 10까지 곱
facto = 1
for i in range(1, 11):
    facto *= i
    print("i =", i, ", facto =", facto)
print("곱 결과 :", facto)
"""

