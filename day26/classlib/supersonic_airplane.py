from day26.classlib.airplane import AirPlane


class SuperSonicAirPlane(AirPlane):
    # 클래스 상수
    NORMAL = 1
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirPlane.NORMAL

    # 오버라이딩(Overriding) - 메서드 재정의
    def fly(self):
        if self.fly_mode == SuperSonicAirPlane.SUPERSONIC:
            print("초음속 비행합니다.")
        else:
            # print("비행기가 일반 비행합니다.")
            # 부모 메서드 상속 받음
            super().fly()   
