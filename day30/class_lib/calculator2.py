# MoreCalculator
from day30.class_lib.calculator import Calculator


class MoreCalculator(Calculator):
    # pass
    def div(self):  # 매서드 재정의(Overriding)
        if self.y == 0:
            return 0
        else:
            return self.x / self.y

    def pow(self):
        return self.x ** self.y


cal = MoreCalculator(10, 4)
print(cal.div())
print(cal.pow())

# 0으로 나눌때 return 0
cal2 = MoreCalculator(10, 0)
print(cal2.div())
print(cal2.pow())