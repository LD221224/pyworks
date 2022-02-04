# 내장 함수

# all() - 0이 없으면 참
print(all([1, 5, 3]))
print(all([1, 0, 3]))

# any() - 모두 0일때 거짓
print(any([1, 2, 0]))

# round(n, digit) - digit : 소수 자릿수 설정(생략 시 정수)
print(round(4.6))
print(round(4.67, 1))

# eval() - 문자열을 숫자로 변환
x = 1
print(eval("x + 1"))

# list(str) - 문자열을 리스트로 변환
print(list("python"))

# sum(iterable) - 반복 가능한 자료 더하기
print(sum([70, 80, 90]))

# min(iterable) - 최솟값
print(min([70, 80, 90]))

# pow() - 거듭 제곱
print(pow(2, 4))