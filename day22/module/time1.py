import time

print(time.time())  # 1970. 1.1  자정 이후부터 현재까지의 시간을 초로 반환
print(time.ctime()) # 날짜와 시간 표기(current time)

year = round(time.time() / (365 * 24 * 60 * 60))    # 반올림
day = time.time() / (24 * 60 * 60)

print(year)
print(day)

# 수행시간 측정하기 - 시작시간 ~ 종료시간
start = time.time()
for i in range(1, 11):
    print(i)
    time.sleep(1)   # time.sleep(초) - 대기시간
end = time.time()

# print("수행 시간 : " + str(end - start) + "초")
print("수행 시간 : %.2f초" % (end - start))