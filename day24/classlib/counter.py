# Counter 클래스 정의와 사용

class Counter:
    def __init__(self):
        self.x = 0  # 인스턴스 멤버 변수
        self.x += 1


c1 = Counter()
print(c1.x)  # c1.x = 1

c2 = Counter()
print(c2.x)  # c2.x = 1
