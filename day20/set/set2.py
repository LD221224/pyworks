# 중복 자료 제거하기

a = [1, 1, 1, 2, 2, 3, 3, 3]
print(a)

# 집합 자료형으로 변환 - set(list) : list -> set
a_set = set(a)
print(a_set)

# 리스트로 변환 - list(set) : set -> list
print(list(a_set))
