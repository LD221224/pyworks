# 리스트 내포(List comprehension)
# [표현식 for 항목 in list]

a = [1, 2, 3, 4, 5]
a2 = []
a3 = []
a4 = []

# a의 짝수를 3의 배수로 저장
for i in a:
    if i % 2 == 0:
        a2.append(i * 3)
print("a2 =", a2)

# 3의 배수로 저장
a3 = [i * 3 for i in a]
print("a3 =", a3)

# a의 짝수를 3의 배수로 저장
a4 = [i * 3 for i in a if i % 2 == 0]
print("a4 =", a4)