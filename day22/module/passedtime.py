import datetime

print("♣ 지금까지 며칠? ♣")
day1 = datetime.date(2021, 12, 26)
print(day1)

today = datetime.date.today()

passedtime= today - day1
print(passedtime)
print("개강 이후 {}일이 지났습니다.".format(passedtime.days))
