from bs4 import BeautifulSoup

html_str = """
<html>
<body>
    <ul class='item'>
        <li>인공지능</li>
        <li>Big Data</li>
        <li>로봇</li>
    </ul>
    <ul class='lang'>
        <li>파이썬</li>
        <li>자바</li>
        <li>자바스크립트</li>
    </ul>
</body>
</html>
"""

# findAll() 사용
soup = BeautifulSoup(html_str, 'html.parser')

ul = soup.find("ul")
lis = ul.findAll("li")
print(lis)  # [<li>인공지능</li>, <li>Big Data</li>, <li>로봇</li>]
print(lis[0])  # <li>인공지능</li>
print(lis[1].text)  # Big Data

ul2 = soup.find("ul", attrs={'class': 'lang'})
print(ul2)
lis2 = ul2.findAll('li')
print(lis2)  # [<li>파이썬</li>, <li>자바</li>, <li>자바스크립트</li>]
print(lis2[2].text)

uls = soup.findAll("ul")
# print(uls)
