# 클래스 정의와 사용

class Student:
    def __init__(self):
        self.name = "콩쥐"    # 멤버 변수
        self.grade = 1

    def learn(self):
        print("수업을 듣습니다.")


s = Student()   # 인스턴스 = 클래스()

print("이름 :", s.name)
print("학년 :", s.grade)
s.learn()
