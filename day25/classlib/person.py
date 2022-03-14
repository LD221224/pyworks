# 정보 은닉(Information Hide)
# 멤버 변수 앞에 언더스코어 1, 2개 있으면 접근 불가(private 속성)

class Person:
    def __init__(self):
        self._name = ""
        self._age = 0


p1 = Person()
# p1. 멤버 변수에 접근 불가(_name, _age)
