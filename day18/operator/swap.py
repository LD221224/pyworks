# 변수 값 교환 프로그램
# 파란 상자에는 1 저장, 빨간 상자에는 2 저장 -> 값 바꾸기
blue = 1
red = 2

# 출력
print('교환 전')
print('blue =', blue, ', red =', red)

# 변수 값 바꾸기 - 임시 변수 temp
"""
temp = blue
blue = red
red = temp
"""

# 파이썬 교환 처리
blue, red = red, blue

# 출력
print('교환 후')
print('blue =', blue, ', red =', red)
