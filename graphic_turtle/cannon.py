# 거북이 대포 게임
import turtle as t
import random as r

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    while t.ycor() > 0: # 거북이가 땅에 닿기까지 반복
        t.forward(15)
        t.right(5)      # 포물선을 그림

t.shape()

# 땅 그리기
t.goto(-300, 0)
t.goto(300, 0)

# 목표 지점
target = r.randint(50, 150)
t.pensize(2)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

# 발사 위치
t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

# 대포 방향 조절
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")     # space는 소문자로 표기
t.listen()

t.mainloop()