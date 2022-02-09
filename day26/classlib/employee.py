from day26.classlib.person import Person


class Employee(Person):
    def __init__(self, name, age, employee_id):
        # super() - 부모 멤버 상속
        super().__init__(name, age)
        self.employee_id = employee_id

    def getid(self):
        return self.employee_id


emp1 = Employee("김산", 31, 1001)
print("이름 :", emp1.getname())
print("나이 :", emp1.getage())
print("사번 :", emp1.getid())
