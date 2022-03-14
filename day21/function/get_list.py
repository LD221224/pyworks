# 리스트를 매개변수로 전달하여 계산

def get_list(a):
    a2 = []
    for i in a:
        a2.append(i * 3)
    return a2


def get_avg(a):
    sum_v = 0
    for i in a:
        sum_v += i
    avg = sum_v / len(a)
    return avg


v = [1, 2, 3, 4, 5]

# v 요소에 3을 곱해 v2 리스트에 저장
v2 = get_list(v)

# v 요소의 평균 계산
average = get_avg(v)

print("v2 =", v2)
print("v 리스트의 평균 :", average)
