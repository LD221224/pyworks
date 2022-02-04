# 기본 매개변수
def sayhello(text, count = 1):
    for i in range(count):
        print(text)

sayhello("Hello")
sayhello("Hello", 3)

# 가변 매개변수 - *리스트로 저장
def calc_sum(*number):
    sum_v = 0
    for i in number:
        sum_v += i
    return sum_v

print(calc_sum(1, 2))
print(calc_sum(1, 2, 3, 4))

# 키워드 매개변수 - **딕셔너리로 저장
def print_kw(**kwargs):
    print(kwargs)

print_kw(name = "지민")
print_kw(name = "지민", age = 30)