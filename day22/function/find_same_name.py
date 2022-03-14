# 동명이인 찾기 - 중복 검사

def find_same_name(a):
    same_name = []
    n = len(a)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                same_name.append(a[i])
    return same_name


'''
    a[0] == a[1], a[0] == a[2], a[0] == a[3], a[0] == a[4] -> 중복
    a[1] == a[2], a[1] == a[3] -> 중복, a[1] == a[4]
    a[2] == a[3], a[2] == a[4]
'''

name = ['콩쥐', '흥부', '팥쥐', '흥부', '콩쥐']
result = find_same_name(name)
print(result)
