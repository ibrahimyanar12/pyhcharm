import turtle as t
from idlelib.configdialog import font_sample_text

t.bgcolor("black")
t.pensize(5)
t.speed(1)
t.color("white")
t.left(150)
t.forward(180)
t.circle(-90,180)
t.setheading(60)
t.circle(-90,180)
t.forward(180)
t.end_fill()
t.hideturtle()
msg="    LEYDİMMMM"
t.write(msg,move=True,align="left")
font=("Arial",25,"italic","bold")


