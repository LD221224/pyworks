# 구구단을 출력하는 함수

def print_gugu(dan):
    for i in range(1, 10):
        # print(dan, "x", i, "=", dan * i)
        print("%d x %d = %d" % (dan, i, dan * i))   # 변수 그룹 괄호로 묶기

print_gugu(6)
