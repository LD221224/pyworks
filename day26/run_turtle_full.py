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

def start():
    global playing
    if playing == False:
        # 게임 시작
        playing = True
        # 화면 지우기
        t.clear()
        # play 함수 호출
        play()

def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 16))
    t.home()

def play():
    global playing
    global score

    if playing:
        t.ontimer(play, 100)

    # 주인공 거북이 속도
    t.forward(10)

    # 적 거북이 방향
    # 1 ~ 5 중에서 2일 확률로(20%)
    if random.randint(1, 5) == 2:
        # 주인공 거북이를 따라온다
        angle = te.towards(t.pos())
        te.setheading(angle)    
        
    # 적 거북이 속도
    speed = score + 5
    te.forward(speed)

    # 먹이에 닿으면
    if t.distance(tf) < 12:
        # 점수를 올리고 화면에 출력
        score += 1
        t.write(score)

        # 먹이의 위치 이동
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x, y)

    # 적 거북이에 닿으면
    if t.distance(te) < 12:
        # 화면에 출력
        text = "Score : " + str(score)
        message("Game over", text)
        # 게임 종료
        playing = False
        score = 0

# 점수, 게임 스위치 변수
playing = False
score = 0

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
t.onkeypress(start, "space")
t.listen()

message("Turtle Run", "[space]")

t.mainloop()