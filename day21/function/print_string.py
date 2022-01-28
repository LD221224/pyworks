# 기본 매개변수
"""
매개변수를 초기화하여 선언하고,
함수 호출 시 매개변수를 생략하면 기본값으로 출력된다.
"""

def print_string(text, count = 1):  # count 없을 때 1
      for i in range(count):
          print(text)

print_string("Hello")   # count = 1
print("=" *  30)
print_string("Hello", 3)

