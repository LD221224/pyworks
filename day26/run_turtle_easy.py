import turtle as t
import random


def turn_right():
    t.setheading(0)


def turn_up():
    t.setheading(90)


def turn_left():
    t.setheading(180)


def turn_down():
    t.setheading(270)


def play():
    # 주인공 거북이 10픽셀 이동
    t.forward(10)

    # 적 거북이의 방향을 주인공 거북이로
    angle = te.towards(t.pos())
    te.setheading(angle)
    # 적 거북이 9픽셀 이동
    te.forward(9)

    # 주인공 거북이와 적 거북이의 거리
    if t.distance(te) >= 12:
        # 0.1초 간격으로 play 콜백
        t.ontimer(play, 100)

    # 주인공 거북이가 먹이에 닿으면
    if t.distance(tf) < 12:
        # 먹이를 랜덤한 위치로 이동
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x, y)


# 주인공 거북이
t.shape("turtle")
t.setup(500, 500)
t.bgcolor("skyblue")
t.color("white")
t.speed(0)
t.up()

# 적 거북이
te = t.Turtle()
te.shape("turtle")
te.color("yellow")
te.speed(0)
te.up()
te.goto(0, 200)

# 먹이
tf = t.Turtle()
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0, -200)

# 방향키
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()

play()

t.mainloop()
