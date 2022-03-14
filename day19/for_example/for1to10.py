# 1부터 10까지 출력
# range(초깃값, 종료값 -1, 증감값)
# 증가값이 1일때 생략 가능
# 초깃값을 생략하면 0부터 시작
for i in range(1, 11, 2):
    print(i, end=' ')  # 1 3 5 7 9
print()

for i in range(1, 11):
    print(i, end=' ')  # 1 2 3 4 5 6 7 8 9 10
print()

for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

# 5보다 큰 수 
for i in range(1, 11):
    if i > 5:
        print(i, end=' ')  # 6 7 8 9 10
print()

# 3의 배수
for i in range(1, 11):
    if i % 3 == 0:
        print(i, end=' ')  # 3 6 9
