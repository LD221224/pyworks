# 키보드로 거북이 조종하기
import turtle as t

def turn_right():
    t.setheading(0)     # 거북이 머리 방향
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def clear():
    t.clear()           # 선 지우기

t.shape("turtle")

# 함수 호출 시 괄호 생략, key 첫글자 대문자 주의
t.onkeypress(turn_right, "Right")   # 오른쪽
t.onkeypress(turn_up, "Up")         # 위
t.onkeypress(turn_left, "Left")     # 왼쪽
t.onkeypress(turn_down, "Down")     # 아래
t.onkeypress(clear, "Escape")       # 지우기

t.listen()  # 실행 대기

t.mainloop()