import datetime

now = datetime.datetime.today()
print(now)
print("{}년".format(now.year))
print(str(now.year) + "년")

today = datetime.date.today()
print(today)

theday = datetime.date(2022, 3, 13)
print(theday)

# 특정 날짜의 요일 알기
days = ['월', '화', '수', '목', '금', '토', '일']

# 요일 - 0 월요일, 1 화요일, ... , 6 일요일
week_idx = datetime.date(2022, 3, 12).weekday()
print(week_idx)
print(days[week_idx] + '요일')


def get_weekday(yyyy, mm, dd):
    days = ['월', '화', '수', '목', '금', '토', '일']
    week_idx = datetime.date(yyyy, mm, dd).weekday()
    print(days[week_idx] + '요일')


get_weekday(2022, 3, 14)
