# 두 수를 입력받아 계산하기
'''
x = int(input("첫째 수 입력 : "))
y = int(input("두번째 수 입력 : "))
'''

x = input("첫째 수 입력 : ")
y = input("두번째 수 입력 : ")

add = int(x) + int(y)
print("두 수의 합 :", add, "입니다.")
print("두 수의 합 : " + str(add) + "입니다.")
# ','로 연결 시 뒤에 띄어쓰기 들어감
# '+'로 문자열 연결할 때 숫자형은 다시 문자형으로 변환
