import turtle
t=turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.shapesize(1)
x=1
t.penup()
for i in range (1000):
    t.fd(2)
    t.lt(8)
    t.shapesize(x)
    x=x+1