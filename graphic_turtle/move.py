import turtle

turtle.shape("turtle")
turtle.color("blue")

# 이동 - forward(거리), right(각도)
"""
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
"""

# for 사용
# 사각형
for i in range (4):
    turtle.forward(100)
    turtle.right(90)

turtle.color("red")

# 삼각형
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.color("green")

# 원 - circle(반지름)
turtle.circle(50)

turtle.mainloop()