0# Dog 클래스 정의와 사용

class Dog:
    type = "진돗개"          # 클래스 (멤버) 변수 - 모든 Dog 공유

    def __init__(self, name):
        self.name = name    # 인스턴스 (멤버) 변수
        # self.type = type


dog1 = Dog("백구")
dog2 = Dog("검둥이")

print(dog1.name)
# 클래스 변수는 클래스 이름으로 직접 접근
# print(dog1.type)
print(Dog.type)

print(dog2.name)
print(Dog.type)