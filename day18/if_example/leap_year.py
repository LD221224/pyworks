# 윤년을 판별하는 프로그램
# 조건 : 윤년은 4년마다 오며, 100년 단위는 윤년이 아니지만 400년 단위는 윤년이다.

year = int(input("년도를 입력하세요 : "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("윤년입니다.")
else:
    print("평년입니다.")
