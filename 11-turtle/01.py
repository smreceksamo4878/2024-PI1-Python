import turtle, random
t=turtle.Turtle()
turtle.bgcolor("black")
t.pos()
(0,0)
t.heading()
0
t.speed(0)

x=1
for i in range(100):
    t.pencolor(f'#{random.randrange(256**3):06x}')
    t.fd(x)
    t.lt(90)
    x=x+5

turtle.mainloop()