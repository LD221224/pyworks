# raise 구문 - 예외 미뤄두기
# 사용하는 곳에서 예외 처리

class Animal:
    # 기본 생성자(멤버 변수가 없을 때) 생략
    def cry(self):
        # print("동물이 웁니다.")
        # 아직 구현되지 않음, 상속 받는 곳에서 구현 필수
        raise NotImplemented


class Dog(Animal):
    # pass
    def cry(self):
        print("왈~ 왈~")


class Cat(Animal):
    # pass
    def cry(self):
        print("야~ 옹!")


dog = Dog()
dog.cry()

cat = Cat()
cat.cry()
