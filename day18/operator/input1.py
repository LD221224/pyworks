# 입력 함수 input()
"""
print("문자 입력 : ")
ch = input()
print(ch)
"""
ch = input("문자 입력 : ")
print(ch)

# 숫자 입력
"""
num = input("숫자 입력 : ") # 문자로 입력됨
num = int(num)  # 문자를 숫자로 변환
print(num + 1)
"""
num = int(input("숫자 입력 : "))
print(num + 1)
print(num > 10)

num2 = float(input("숫자 입력 : "))
print(num2 + 1)
print(num2 > 10.1)
