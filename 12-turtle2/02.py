import turtle, random
t=turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.delay(0)
x=-400
y=250
t.pu()
t.setpos(x, y)
t.pd()

d=60

poc_dom=7

def stvorec(d):
    for i in range(4):
        t.fd(d)
        t.lt(90)

def dom(d):
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    stvorec(d)
    t.end_fill()
    t.pu()
    t.lt(90)
    t.fd(d/4)
    t.rt(90)
    t.fd(d/4)
    t.pd()
    okno()
    t.pu()
    for i in range(2):
        t.lt(90)
        t.fd(d/4*3)
    t.pd()
    strecha(d)
    t.pu()
    t.lt(150)
    t.fd(d)
    t.lt(90)
    t.fd(d/2)
    t.pd()
    
def okno():
    t.fillcolor("white")
    t.begin_fill()
    stvorec(d/4)
    t.end_fill()
    t.fd(d/4)
    for i in range(3):
        t.fillcolor("white")
        t.begin_fill()
        stvorec(d/4)
        t.end_fill()
        t.fd(d/4)
        t.lt(90)
        t.fd(d/4)
    t.fd(d/4)
    
def strecha(d):
    t.lt(30)
    t.fillcolor("black")
    t.begin_fill()
    for i in range(3):
        t.fd(d)
        t.lt(120)
    t.end_fill()

def ulica(poc_dom):
    for i in range(poc_dom):
        dom(d)
    t.pu()
    t.bk(d*poc_dom + d/2*poc_dom)
    t.rt(90)
    t.fd(d*2)
    t.lt(90)
    t.pd()

def dedina(poc_ul):
    for i in range(poc_ul):
        ulica(9)

dedina(6)
    
turtle.exitonclick()