# 랜덤 위치로 이동
import random as r
import turtle as t

t.shape("turtle")
t.speed(0)
t.up()

x = r.randint(-500, 500)
y = r.randint(-500, 500)
t.goto(x, y)

t.mainloop()
