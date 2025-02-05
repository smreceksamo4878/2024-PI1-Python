import turtle
t=turtle.Turtle()
t.speed(0)
turtle.delay(0)

def uholnik(n,d):
    for i in range(n):
        t.fd(d)
        t.lt(360/n)

for n in range(3,30):
    uholnik(n,50)

turtle.exitonclick()