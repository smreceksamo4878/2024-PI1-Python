import turtle
t=turtle.Turtle()
t.speed(0)

n=20
d=5

def schod(n, d):
    for i in range(n):
        t.fd(d)
        t.rt(90)
        t.fd(d)
        t.lt(90)

for i in range(4):
    schod(n, d)
    t.penup()
    t.lt(90)
    t.fd(n*d)
    t.pendown()
    t.rt(90)


turtle.exitonclick()