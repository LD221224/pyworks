# 거듭 제곱 함수 만들기
def mypow(x, y):
    result = 1
    for i in range(0, y):
        result *= x
    return result

# 절댓값 함수 만들기
def myabs(x):
    if x < 0:
        return -x
    else:
        return x

if __name__=="__main__":
    print(mypow(2, 4))
    print(mypow(5, 3))
    print(myabs(-10))