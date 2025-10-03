from turtle import *
color("orange")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('lightgreen')

    pen.write("eslem yanar", font=("Verdana", 12, "bold"))

end_fill()
done()
