# return이 있는 함수의 정의와 호출

# 1 증가 함수
def one_up(x):
    return x + 1

# 두 수의 차를 구하는 함수
def sub(x, y):
    return x - y

# 절댓값을 구하는 함수
def my_abs(a):
    if a < 0:
        return -a
    else:
        return a

num = one_up(1)
print(num)

num2 = sub(5, 6)
print(num2)

num3 = my_abs(-10)
num4 = my_abs(10)
print(num3)
print(num4)

# 내장 함수 abs()
print(abs(-10))
