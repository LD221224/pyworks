# requests - python 프로그래밍 언어용 http 라이브러리
import requests

url = "https://www.python.org/"
# 200 - 페이지 요청 성공
# 404 - 페이지 없음
response = requests.get(url)
print(response)
print(response.status_code)

html = response.text
print(html)
